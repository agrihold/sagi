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

class information(osv.osv):
    """"""
    
    _name = 'sgr.information'
    _description = 'information'
    _inherits = {  }
    _inherit = [ 'mail.thread' ]

    def _get_name(self, cr, uid, ids, name, args, context=None):
        """se calcula como la categoría de la infomracion mas el nombre del producto o el nombre del partner"""
        raise NotImplementedError

    _states_ = [
        # State machine: information
        ('draft','Draft'),
        ('approved','Approved'),
        ('depreciated','Depreciated'),
        ('cancelled','Cancelled'),
    ]
    _track = {
        'state': {
            'sgr.information_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.information_approved': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'approved',
            'sgr.information_depreciated': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'depreciated',
            'sgr.information_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
        },
    }
    _columns = {
        'name': fields.function(_get_name, type='char', arg=None, fnct_inv_arg=None, obj=None, string='Name', readonly=True, size=128, states={'draft': [('readonly', False)]}),
        'partner_id': fields.many2one('res.partner', string='Partner', readonly=True, states={'draft': [('readonly', False)]}),
        'product_id': fields.many2one('product.product', string='Product', readonly=True, states={'draft': [('readonly', False)]}),
        'text': fields.html(string='Text', readonly=True, required=True, states={'draft': [('readonly', False)]}),
        'company_id': fields.many2one('res.company', string='Company'),
        'state': fields.selection(_states_, "State"),
        'document_id': fields.many2one('sgr.document', string='document_id', ondelete='cascade'), 
        'information_category_id': fields.many2one('sgr.information_category', string='Category', readonly=True, required=True, states={'draft': [('readonly', False)]}, domain=[('hierachical_type','=','normal')]), 
        'information_presentation_ids': fields.one2many('sgr.information_presentation', 'parent_information_id', string='information_presentation_ids'), 
    }

    _defaults = {
        'state': 'draft',
        'company_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.information', context=c),
    }

    _order = "id desc"

    _constraints = [
    ]


    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.information', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.information', obj_id, cr)
        return True



information()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
