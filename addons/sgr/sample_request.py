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

class sample_request(osv.osv):
    """"""
    
    _name = 'sgr.sample_request'
    _description = 'sample_request'
    _inherits = {  }
    _inherit = [ 'mail.thread' ]

    _states_ = [
        # State machine: sample_request
        ('draft','Draft'),
        ('requested','Requested'),
        ('done','Done'),
        ('cancelled','Cancelled'),
    ]
    _track = {
        'state': {
            'sgr.sample_request_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.sample_request_requested': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'requested',
            'sgr.sample_request_done': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'done',
            'sgr.sample_request_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
        },
    }
    _columns = {
        'name': fields.char(string='Reference', readonly=True, size=32),
        'product_id': fields.many2one('product.product', string='Product', required=True),
        'supplier_id': fields.many2one('res.partner', string='Supplier', required=True, context={'default_supplier':'True','default_is_company':'True'}, domain=[('supplier','=',True)]),
        'amount': fields.float(string='Amount', required=True),
        'amount_uom_id': fields.many2one('product.uom', string='UOM', required=True),
        'concentration': fields.float(string='Concentration'),
        'concentration_uom_id': fields.many2one('product.uom', string='UOM'),
        'import_license': fields.char(string='Import License', size=64),
        'date_of_import_license': fields.date(string='Date of import license'),
        'expiration_date_of_import': fields.date(string='Expiration date of import license'),
        'deadline': fields.date(string='Deadline'),
        'departure': fields.date(string='Departure'),
        'note': fields.text(string='Note'),
        'location_id': fields.many2one('stock.location', string='Final Destination', domain=[('usage','!=','view')]),
        'specific_batch': fields.selection([(u'yes', u'Yes'), (u'no', u'No')], string='Specific Batch', required=True),
        'batch': fields.char(string='Batch', size=64),
        'state': fields.selection(_states_, "State"),
        'product_in_ret_id': fields.many2one('sgr.product_in_ret', string='RET'), 
        'packaging_ids': fields.one2many('sgr.packaging', 'sample_request_id', string='Packagings'), 
        'move_ids': fields.many2many('stock.move', 'sgr___move_ids_rel', 'sample_request_id', 'move_id', string='Stock Moves'), 
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
            wf_service.trg_delete(uid, 'sgr.sample_request', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.sample_request', obj_id, cr)
        return True



sample_request()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
