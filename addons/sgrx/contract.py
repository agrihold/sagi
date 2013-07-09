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

import logging
_logger = logging.getLogger(__name__)

class contract(osv.osv):
    """"""
    _name = 'sgr.contract'
    _inherit = [ _name ]

    _columns = {
        'line_ids': fields.related(
                    'analytic_account_id',
                    'line_ids',
                    type='one2many',
                    relation='account.analytic.account',
                    string='line_ids'
                    ),
    }

    def approve_contract(self, cr, uid, ids, context=None):
        """
        Create analytic journal for this contract. Must be called by the workflow when change from received state to approved.
        1) create a child account.analytic.account to the partner account.analytic.account.
        2) must create account.analytic.line with ammount stored in value.
        De skype:

[14h'45:55] Juan José Scarafía: 1. Al validar un contrato de ese laboratorio deberíamos crera una cuenta analítia hija de la cuenta view del partner
[14h'46:25] Juan José Scarafía: mirando las cuentas anliticas tendríamos para cada laboratorio una cuenta tipo view
[14h'46:38] Juan José Scarafía: y tantas cuentas analiticas hijas de esa view como contratos aprobados tenga el laboratorio
[14h'47:46] Cristian Sebastian Rocha: Proyectos hace eso también, no?
[14h'48:02] Juan José Scarafía: mmm, si, de cierta forma sí
[14h'48:16] Juan José Scarafía: pero proyecto hereda de cuentas analiticas y además crea una referencia a una cuenta analitica

[14h'48:51] Juan José Scarafía: sería basicamente eso
[14h'49:28] Juan José Scarafía: tenemos: 
1. Laboratorios --> Cuenta analitica tipo view
2. Contratos --> Cuenta analiticas normales (hijas de 1)
3. Proposal --> Asientos analticios dentro del contrato (cuenta analitica del punto 2)
[14h'49:49] Juan José Scarafía: [hice un push, por si querés bajar algunas actualizaciones]
[16h'28:35] Juan José Scarafía: 3) Al aprobar una proposal, se deben crear studys un study para cada "product_study" de esa proposal. En el study se completa: producto, laboratorio, categoria de estudio (todo eso viene de la proposal) y le definis source='own'
[16h'29:47] Juan José Scarafía: 4) Cuando uno va al menu "studies" solo puede crear Studies que sean source='supplier'. Los studies tipo 'own' se crean desde una proposal
        """
        context=context or {}
        analytic_obj = self.pool.get("account.analytic.account")
        analytic_line_obj = self.pool.get("account.analytic.line")
        for con in self.browse(cr, uid, ids):
            if not con.analytic_account_id:
                value = {
                    'name': con.name,
                    'code' : con.pool.get('ir.sequence').next_by_code(cr, uid, 'sgr.contract.analytic.account'),
                    'type': 'normal',
                    'parent_id': con.property_analytic_account_root_id.id,
                    'partner_id': con.laboratory_id.id,
                    'user_id': False,
                    'manager_id': False,
                    'company_id': con.company_id.id,
                    'state': 'open',
                    'currency_id': con.company_id.currency_id.id,
                }
                ana_id = analytic_obj.create(cr, uid, value)
            value = {
                'name': con.name,
                'amount': con.amount,
                'account_id': ana_id,
                'general_account_id': con.property_general_account_id.id,
                'journal_id': con.property_journal_id.id,
            }
            line_id = analytic_line_obj.create(cr, uid, value)
            self.write(cr, uid, con.id, {'analytic_account_id': ana_id,
                'state': 'approved'})
        return True

    def cancel_contract(self, cr, uid, ids, context=None):
        """
        new account.analitic.line with -value in amount
        account.analytic.account.status := cancel
        """
        context=context or {}
        analytic_line_obj = self.pool.get("account.analytic.line")
        analytic_obj = self.pool.get("account.analytic.account")
        for con in self.browse(cr, uid, ids):
            if con.proposal_ids:
                raise osv.except_osv(u'Error', u'Can\'t cancel contract \'%s\' with proposals.' % con.name) 
            if con.state == 'approved':
                line_ids = analytic_line_obj.search(cr, uid, [('account_id','=',con.analytic_account_id.id)])
                analytic_line_obj.unlink(cr, uid, line_ids)
                analytic_obj.unlink(cr, uid, [con.analytic_account_id.id])
            self.write(cr, uid, con.id, {'state': 'cancelled', 'analytic_account_id': False})

contract()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
