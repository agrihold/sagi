# -*- coding: utf-8 -*-
##############################################################################
#
#    SGR. Sistema de Gestion de Registros
#    Copyright (C) 2013 Grupo ADHOC
#    No email
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


import re
import netsvc
from osv import osv, fields

class proposal(osv.osv):
    """"""
    _name = 'sgr.proposal'
    _inherit = [ _name ]

    def _get_amount(self, cr, uid, ids, name, args, context=None):
        v = {}
        for p in self.browse(cr, uid, ids):
            v[p.id] = sum( pp.sub_total for pp in p.proposal_product_ids )
        return v

    _columns = {
        'amount': fields.function(_get_amount, store=True, type='float', arg=None, fnct_inv_arg=None, obj=None, string='Amount', readonly=True),
    }

    def approve_proposal(self, cr, uid, ids, context=None):
        """Si la proposal.type = by_contract debe exigir contrato.
Si la proposal.type = on_demand no debe haber contrato.

        De skype:
[14h'48:47] Juan José Scarafía: 2) Cuando se aprueba una proposal (del tipo "by_contract"), se debe generar un asiento analíticio dentro de la cuenta analitica del contrato elegido en esta proposal
[16h'28:35] Juan José Scarafía: 3) Al aprobar una proposal, se deben crear studys un study para cada "product_study" de esa proposal. En el study se completa: producto, laboratorio, categoria de estudio (todo eso viene de la proposal) y le definis source='own'
[16h'29:47] Juan José Scarafía: 4) Cuando uno va al menu "studies" solo puede crear Studies que sean source='supplier'. Los studies tipo 'own' se crean desde una proposal
"""
        context=context or {}
        analytic_line_obj = self.pool.get("account.analytic.line")
        study_obj = self.pool.get("sgr.study")
        for pro in self.browse(cr, uid, ids):
            v = { 'state': 'approved' }
            if pro.type == 'by_contract':
                con = pro.contract_id

                if not con:
                    raise osv.except_osv(u'Error',
                                         u'You must assign a contract to "%s" or change his type.' % pro.name)

                if con.analytic_account_id.balance - pro.amount < 0.0:
                    raise osv.except_osv(u'Error',
                                         u'Contract \'%s\' has %f of cash. It has not enought amount for proposal \'%s\'.' %
                                         (con.name, con.analytic_account_id.balance, pro.name))

                #
                # Crear Linea analítica
                #
                value = {
                    'name': pro.name,
                    'amount': -pro.amount,
                    'account_id': con.analytic_account_id.id,
                    'general_account_id': con.property_general_account_id.id,
                    'journal_id': con.property_journal_id.id,
                }
                line_id = analytic_line_obj.create(cr, uid, value)
                v['analytic_line_id'] = line_id

            #
            # Crear Estudios
            #
            for pp in pro.proposal_product_ids:
                for ps in pp.product_study_ids:
                    sv = {
                        'name': ps.study_category_id.name,
                        'product_id': pp.product_id.id,
                        'source': 'own',
                        'laboratory_id': pro.laboratory_id.id,
                        'start_date': False,
                        'end_date': False,
                        'concentration': False,
                        'concentration_uom_id': False,
                        'director_author_id': False,
                        'summary': False,
                        'result': False,
                        'validation_method': False,
                        'proposal_id': pro.id,
                        'product_studies': ps.id,
                        'document_category_id': ps.study_category_id.id,
                    }
                    std_id = study_obj.create(cr, uid, sv)
                    wf_service = netsvc.LocalService("workflow")
                    wf_service.trg_validate(uid, 'sgr.study', std_id, 'sgn_contract', cr)
                    ps.write({'study_id': std_id})
            self.write(cr, uid, pro.id, v)

    def cancel_proposal(self, cr, uid, ids, context=None):
        context=context or {}
        analytic_line_obj = self.pool.get("account.analytic.line")
        for pro in self.browse(cr, uid, ids):
            v = { 'state': 'cancel' }
            if pro.type == 'by_contract':
                if not pro.contract_id:
                    raise osv.except_osv(u'Error',
                                         u'I expect a contract for "%s". Something is wrong. Contact your administrator.' % pro.reference)
                con = pro.contract_id
                value = {
                    'name': pro.reference,
                    'amount': pro.amount,
                    'account_id': con.analytic_account_id.id,
                    'general_account_id': con.property_general_account_id.id,
                    'journal_id': con.property_journal_id.id,
                }
                line_id = analytic_line_obj.create(cr, uid, value)
                v['analytic_line_id'] = False
            self.write(cr, uid, pro.id, v)

    def onchange_contract_id(self, cr, uid, ids, type, contract_id, context=None):
        context = context or {}
        if type == 'by_contract' and contract_id:
            contract_obj = self.pool.get('sgr.contract').browse(cr, uid, contract_id)
            return { 'value': { 'currency_id': contract_obj.currency_id.id } }
        else:
            return {}

proposal()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
