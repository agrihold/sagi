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

class contract(osv.osv):
    """"""
    
    _name = 'sgr.contract'
    _description = 'contract'
    _inherits = {  }
    _inherit = [ 'mail.thread','ir.needaction_mixin' ]

    _states_ = [
        # State machine: contract
        ('draft','Draft'),
        ('requested','Requested'),
        ('received','Received'),
        ('approved','Approved'),
        ('solved','Solved'),
        ('cancelled','Cancelled'),
    ]
    _track = {
        'state': {
            'sgr.contract_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.contract_requested': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'requested',
            'sgr.contract_received': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'received',
            'sgr.contract_approved': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'approved',
            'sgr.contract_solved': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'solved',
            'sgr.contract_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
        },
    }
    _columns = {
        'date': fields.date(string='Date', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'received': [('readonly', False)]}),
        'name': fields.char(string='Reference', readonly=True, required=True, size=32, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'received': [('readonly', False)]}),
        'laboratory_id': fields.many2one('res.partner', string='Laboratory', readonly=True, required=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'received': [('readonly', False)]}, context={'default_is_laboratory':'True','default_is_company':'True'}, domain=[('is_laboratory','=',True)]),
        'amount': fields.float(string='Values', readonly=True, required=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'received': [('readonly', False)]}),
        'currency_id': fields.many2one('res.currency', string='Currency', readonly=True, required=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'received': [('readonly', False)]}),
        'payment_information': fields.text(string='Payment information'),
        'observations': fields.text(string='Observations'),
        'company_id': fields.many2one('res.company', string='Company', readonly=True, required=True),
        'document_id': fields.binary(string='Contract File', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'received': [('readonly', False)]}),
        'property_general_account_id': fields.property('account.account', string='general_account_id', type='many2one', relation='account.account', method=True, view_load=True, group_name='SGR'),
        'property_analytic_account_root_id': fields.property('account.analytic.account', string='analytic_account_root_id', type='many2one', relation='account.analytic.account', method=True, view_load=True, group_name='SGR'),
        'property_journal_id': fields.property('account.analytic.journal', string='journal_id', type='many2one', relation='account.analytic.journal', method=True, view_load=True, group_name='SGR'),
        'state': fields.selection(_states_, "State"),
        'payment_term_id': fields.many2one('account.payment.term', string='Payment Term', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'received': [('readonly', False)]}, required=True), 
        'analytic_account_id': fields.many2one('account.analytic.account', string='Analytic Account', readonly=True), 
        'proposal_ids': fields.one2many('sgr.proposal', 'contract_id', string='Proposals', readonly=True), 
    }

    _defaults = {
        'state': 'draft',
        'company_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.contract', context=c),
    }

    _order = "id desc"

    _constraints = [
    ]


    def approve_contract(self, cr, uid, ids, context=None):
        """Create analytic journal for this contract. Must be called by the workflow when change from received state to approved.
1) create a child account.analytic.account to the partner account.analytic.account.
2) must create account.analytic.line with ammount stored in value."""
        raise NotImplementedError

    def get_default_company(self, cr, uid, ids, context=None):
        """Return the default company from user."""
        raise NotImplementedError

    def get_default_currency(self, cr, uid, ids, context=None):
        """Return the default currency from user."""
        raise NotImplementedError

    def cancel_contract(self, cr, uid, ids, context=None):
        """new account.analitic.line with -value in amount
account.analytic.account.status := cancel"""
        raise NotImplementedError

    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.contract', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.contract', obj_id, cr)
        return True



contract()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
