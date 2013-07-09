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

class trademark_registry(osv.osv):
    """"""
    
    _name = 'sgr.trademark_registry'
    _description = 'trademark_registry'
    _inherits = { 'sgr.registry':'sgr_registry_id' }
    _inherit = [ 'mail.thread' ]

    _states_ = [
        # State machine: registry
        ('draft','Draft'),
        ('requested','Requested'),
        ('approved','Approved'),
        ('rejected','Rejected'),
        ('depreciated','Depreciated'),
        ('cancelled','Cancelled'),
    ]
    _track = {
        'state': {
            'sgr.trademark_registry_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.trademark_registry_requested': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'requested',
            'sgr.trademark_registry_approved': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'approved',
            'sgr.trademark_registry_rejected': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'rejected',
            'sgr.trademark_registry_depreciated': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'depreciated',
            'sgr.trademark_registry_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
        },
    }
    _columns = {
        'sgr_registry_id': fields.many2one('sgr.registry', 'Registries', ondelete='cascade', required=True, help=u"""Si el registro es una modificación entonces se debe seleccionar un &quot;operate_id&quot;
Si un registro es del tipo operation &quot;replacement&quot;, también se debe seleccionar un registro &quot;operate_id&quot; pero para validar el segundo registor el primero debe estar en estado expirado"""),
        'name': fields.char(string='Name', readonly=True, required=True, size=128, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'product_id': fields.many2one('product.product', string='Product', readonly=True, required=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}, context={'default_function_type':'formulated'}, domain=[('function_type','=','formulated')]),
        'trademark_type_id': fields.many2one('sgr.trademark_type', string='Trademark Type'),
        'state': fields.selection(_states_, "State"),
    }

    _defaults = {
    }

    _order = "id desc"

    _constraints = [
    ]


    def get_registro_types(self, cr, uid, ids, context=None):
        """"""
        member = getattr(self.pool.get('sgr.registry'), 'get_registro_types')
        return member(cr, uid, ids)

    def create_new(self, cr, uid, ids, context=None):
        """"""
        member = getattr(self.pool.get('sgr.registry'), 'create_new')
        return member(cr, uid, ids)

    def onchange_registry_category(self, cr, uid, ids, registry_category_id, context=None):
        """"""
        member = getattr(self.pool.get('sgr.registry'), 'onchange_registry_category')
        return member(cr, uid, ids, registry_category_id)

    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.trademark_registry', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.trademark_registry', obj_id, cr)
        return True

    def unlink(self, cr, uid, ids, context=None):
        sgr_registry_obj = self.pool.get('sgr.registry')
        data = self.read(cr, uid, ids, [ 'sgr_registry_id', ])
        res = super(trademark_registry, self).unlink(cr, uid, ids, context=context)
        for item in data:
            sgr_registry_obj.unlink(cr, uid, item['sgr_registry_id'][0],context=context)
        return res


trademark_registry()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
