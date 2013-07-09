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

class official_letter(osv.osv):
    """"""
    
    _name = 'sgr.official_letter'
    _description = 'official_letter'
    _inherits = {  }
    _inherit = [ 'mail.thread' ]

    _states_ = [
        # State machine: official_letter
        ('draft','Draft'),
        ('sent','Sent'),
        ('received','Received'),
        ('cancelled','Cancelled'),
    ]
    _track = {
        'state': {
            'sgr.official_letter_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.official_letter_sent': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'sent',
            'sgr.official_letter_received': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'received',
            'sgr.official_letter_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
        },
    }
    _columns = {
        'name': fields.char(string='Reference', readonly=True, required=True, size=32, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}),
        'direction': fields.selection([(u'in', u'In'), (u'out', u'Out')], string='Direction', readonly=True, required=True, states={'draft': [('readonly', False)]}),
        'government_agency_id': fields.many2one('res.partner', string='Government Agency', readonly=True, required=True, states={'draft': [('readonly', False)]}, context={'default_is_gov_agency':'True','default_is_company':'True'}, domain=[('is_gov_agency','=',True)]),
        'contact': fields.many2one('res.partner', string='Contact', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}),
        'issue_date': fields.date(string='Issue Date', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}),
        'delivery_date': fields.date(string='Delivery Date', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}),
        'user': fields.many2one('res.partner', string='User', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, context={'default_is_company':'False','default_employee':'True'}, domain=[('employee','=',True)]),
        'tracking_number': fields.char(string='Tracking Number', readonly=True, size=64, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}),
        'protocol': fields.char(string='Protocol', readonly=True, size=32, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}),
        'protocol_date': fields.date(string='Protocol Date', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}),
        'company_id': fields.many2one('res.company', string='Company', readonly=True, required=True),
        'state': fields.selection(_states_, "State"),
        'shipping_method_id': fields.many2one('sgr.shipping_method', string='Shipping Method', readonly=True, required=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}), 
        'comunication_ids': fields.one2many('sgr.communication', 'official_letter_id', string='Communications'), 
    }

    _defaults = {
        'state': 'draft',
        'company_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.official_letter', context=c),
    }

    _order = "id desc"

    _constraints = [
    ]


    def get_default_company(self, cr, uid, ids, context=None):
        """"""
        raise NotImplementedError

    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.official_letter', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.official_letter', obj_id, cr)
        return True



official_letter()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
