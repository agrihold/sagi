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

class document_move(osv.osv):
    """"""
    
    _name = 'sgr.document_move'
    _description = 'document_move'
    _inherits = {  }
    _inherit = [ 'mail.thread' ]

    _states_ = [
        # State machine: document_move
        ('draft','Draft'),
        ('requested','Requested'),
        ('sent','Sent'),
        ('received','Received'),
        ('cancelled','Cancelled'),
    ]
    _track = {
        'state': {
            'sgr.document_move_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.document_move_requested': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'requested',
            'sgr.document_move_sent': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'sent',
            'sgr.document_move_received': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'received',
            'sgr.document_move_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
        },
    }
    _columns = {
        'from_partner': fields.many2one('res.partner', string='From', readonly=True, required=True, states={'draft': [('readonly', False)]}, context={'default_is_company':'True'}, domain=[('is_company','=',True)]),
        'to_partner': fields.many2one('res.partner', string='To', readonly=True, required=True, states={'draft': [('readonly', False)]}, context={'default_is_company':'True'}, domain=[('is_company','=',True)]),
        'from_contact': fields.many2one('res.partner', string='Contact', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'sent': [('readonly', False)]}),
        'to_contact': fields.many2one('res.partner', string='Contact', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'sent': [('readonly', False)]}),
        'requested_date': fields.date(string='Requested Date', readonly=True, states={'draft': [('readonly', False)]}),
        'sent_date': fields.date(string='Sent Date', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'received_date': fields.date(string='Received Date', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'sent': [('readonly', False)]}),
        'tracking_id': fields.char(string='Tracking Number', readonly=True, size=64, states={'draft': [('readonly', False)], 'requested': [('readonly', False)], 'sent': [('readonly', False)]}),
        'state': fields.selection(_states_, "State"),
        'document_id': fields.many2one('sgr.document', string='document_id', ondelete='cascade', required=True), 
    }

    _defaults = {
        'state': 'draft',
    }

    _order = "id desc"

    _constraints = [
    ]


    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.document_move', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.document_move', obj_id, cr)
        return True



document_move()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
