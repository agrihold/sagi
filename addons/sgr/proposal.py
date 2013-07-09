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

class proposal(osv.osv):
    """"""
    
    _name = 'sgr.proposal'
    _description = 'proposal'
    _inherits = {  }
    _inherit = [ 'mail.thread' ]

    def _get_amount(self, cr, uid, ids, name, args, context=None):
        """"""
        raise NotImplementedError

    _states_ = [
        # State machine: proposal
        ('draft','Draft'),
        ('requested','Requested'),
        ('received','Received'),
        ('approved','Approved'),
        ('done','Done'),
        ('cancelled','Cancelled'),
    ]
    _track = {
        'state': {
            'sgr.proposal_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.proposal_requested': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'requested',
            'sgr.proposal_received': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'received',
            'sgr.proposal_approved': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'approved',
            'sgr.proposal_done': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'done',
            'sgr.proposal_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
        },
    }
    _columns = {
        'type': fields.selection([(u'by_contract', u'By Contract'), (u'on_demand', u'On Demand')], string='Type', readonly=True, required=True, states={'draft': [('readonly', False)]}),
        'laboratory_id': fields.many2one('res.partner', string='Laboratory', readonly=True, required=True, states={'draft': [('readonly', False)]}, context={'default_is_laboratory':'True','default_is_company':'True'}, domain=[('is_laboratory','=','True')]),
        'name': fields.char(string='Reference', readonly=True, required=True, size=64, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'received': [('readonly', False)]}),
        'amount': fields.function(_get_amount, type='float', arg=None, fnct_inv_arg=None, obj=None, string='Total Amount', readonly=True),
        'currency_id': fields.many2one('res.currency', string='Currency'),
        'analytic_line_id': fields.many2one('account.analytic.line', string='Analytic Line', readonly=True),
        'company_id': fields.many2one('res.company', string='Company', readonly=True, required=True),
        'state': fields.selection(_states_, "State"),
        'contract_id': fields.many2one('sgr.contract', string='Contract', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'received': [('readonly', False)]}), 
        'sponsor_ids': fields.many2many('res.partner', 'sgr_sponsor_ids_proposal_as_sponsor_ids_rel', 'proposal_id', 'partner_id', string='Sponsors', context={'default_supplier':'True','default_is_company':'True'}, domain=[('supplier','=',True)]), 
        'proposal_product_ids': fields.one2many('sgr.proposal_product', 'proposal_id', string='Items', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'received': [('readonly', False)]}, required=True), 
        'study_ids': fields.one2many('sgr.study', 'proposal_id', string='Studies'), 
    }

    _defaults = {
        'state': 'draft',
        'company_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.proposal', context=c),
    }

    _order = "id desc"

    _constraints = [
    ]


    def approve_proposal(self, cr, uid, ids, context=None):
        """Si la proposal.type = by_contract debe exigir contrato.
Si la proposal.type = on_demand no debe haber contrato."""
        raise NotImplementedError

    def onchange_contract_id(self, cr, uid, ids, intype, incontract_id, context=None):
        """"""
        raise NotImplementedError

    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.proposal', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.proposal', obj_id, cr)
        return True



proposal()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
