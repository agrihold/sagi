# -*- coding: utf-8 -*-
##############################################################################
#
#    SGR
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
from openerp import netsvc
from openerp.osv import osv, fields

class tax(osv.osv):
    """"""
    
    _name = 'sgr.tax'
    _description = 'tax'
    _inherits = { 'sgr.document':'sgr_document_id' }
    _inherit = [ 'mail.thread' ]

    _states_ = [
        # State machine: tax
        ('draft','Draft'),
        ('to_pay','To Pay'),
        ('paid','Paid'),
        ('expired','Expired'),
        ('cancelled','Cancelled'),
    ]
    _track = {
        'state': {
            'sgr.tax_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.tax_to_pay': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'to_pay',
            'sgr.tax_paid': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'paid',
            'sgr.tax_expired': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'expired',
            'sgr.tax_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
        },
    }
    _columns = {
        'sgr_document_id': fields.many2one('sgr.document', 'Documents', ondelete='cascade', required=True, help=u""""""),
        'government_agency_id': fields.many2one('res.partner', string='Government Agency', help=u"""Filtrar por partners tipo government agency""", readonly=True, states={'draft': [('readonly', False)]}, context={'default_is_gov_agency':'True','default_is_company':'True'}, domain=[('is_gov_agency','=',True)]),
        'payment_date': fields.date(string='Payment Date', readonly=True, states={'draft': [('readonly', False)], 'to_pay': [('readonly', False)]}),
        'is_urgent': fields.boolean(string='Is Urgent?', readonly=True, states={'draft': [('readonly', False)], 'to_pay': [('readonly', False)]}),
        'ticket_id': fields.char(string='Ticket N', readonly=True, states={'draft': [('readonly', False)], 'to_pay': [('readonly', False)]}),
        'voucher_id': fields.char(string='Voucher N', readonly=True, states={'draft': [('readonly', False)], 'to_pay': [('readonly', False)]}),
        'amount': fields.float(string='Amount', readonly=True, states={'draft': [('readonly', False)]}),
        'currency_id': fields.many2one('res.currency', string='Currency', readonly=True, states={'draft': [('readonly', False)]}),
        'currency_rate': fields.float(string='Rate', readonly=True, states={'draft': [('readonly', False)], 'to_pay': [('readonly', False)]}),
        'my_amount': fields.float(string='Company Currency Amount', readonly=True),
        'my_currency_id': fields.many2one('res.currency', string='Company Currency', readonly=True),
        'state': fields.selection(_states_, "State"),
        'registry_id': fields.many2one('sgr.registry', string='Registry', ondelete='cascade', required=True), 
        'communication_ids': fields.many2many('sgr.communication', 'sgr_tax_ids_communication_ids_rel', 'tax_id', 'communication_id', string='Communications', readonly=True), 
    }

    _defaults = {
        'state': 'draft',
    }

    _order = "id desc"

    _constraints = [
    ]


    def get_currency_rate(self, cr, uid, ids, context=None):
        """se calcula al cambiar el currency_id. la taza de conversion entre el currnecy_id y el my_currency_id"""
        raise NotImplementedError

    def get_my_amount(self, cr, uid, ids, context=None):
        """se calcula cuando cambia el currency_rate o el amount"""
        raise NotImplementedError

    def get_my_currency_id(self, cr, uid, ids, context=None):
        """se calcula cuando se instancia a partir del valor de la companía"""
        raise NotImplementedError

    def get_default_company(self, cr, uid, ids, context=None):
        """"""
        member = getattr(self.pool.get('sgr.document'), 'get_default_company')
        return member(cr, uid, ids)

    def do_approve(self, cr, uid, ids, context=None):
        """"""
        member = getattr(self.pool.get('sgr.document'), 'do_approve')
        return member(cr, uid, ids)

    def do_depreciate(self, cr, uid, ids, context=None):
        """"""
        member = getattr(self.pool.get('sgr.document'), 'do_depreciate')
        return member(cr, uid, ids)

    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.tax', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.tax', obj_id, cr)
        return True

    def unlink(self, cr, uid, ids, context=None):
        sgr_document_obj = self.pool.get('sgr.document')
        data = self.read(cr, uid, ids, [ 'sgr_document_id', ])
        res = super(tax, self).unlink(cr, uid, ids, context=context)
        for item in data:
            sgr_document_obj.unlink(cr, uid, item['sgr_document_id'][0],context=context)
        return res


tax()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
