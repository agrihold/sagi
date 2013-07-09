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

class formulated_product_registry(osv.osv):
    """"""
    
    _name = 'sgr.formulated_product_registry'
    _description = 'formulated_product_registry'
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
            'sgr.formulated_product_registry_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.formulated_product_registry_requested': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'requested',
            'sgr.formulated_product_registry_approved': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'approved',
            'sgr.formulated_product_registry_rejected': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'rejected',
            'sgr.formulated_product_registry_depreciated': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'depreciated',
            'sgr.formulated_product_registry_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
        },
    }
    _columns = {
        'sgr_registry_id': fields.many2one('sgr.registry', 'Registries', ondelete='cascade', required=True, help=u"""Si el registro es una modificación entonces se debe seleccionar un &quot;operate_id&quot;
Si un registro es del tipo operation &quot;replacement&quot;, también se debe seleccionar un registro &quot;operate_id&quot; pero para validar el segundo registor el primero debe estar en estado expirado"""),
        'operation': fields.selection([(u'new', u'New'), (u'modification', u'Modification'), (u'replacement', u'Replacement')], string='Operation', readonly=True, required=True, states={'draft': [('readonly', False)]}),
        'commercial_name': fields.char(string='Commercial Name', readonly=True, size=128, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'formulated_product_id': fields.many2one('product.product', string='Formulated Product', readonly=True, required=True, states={'draft': [('readonly', False)]}, context={'default_function_type':'formulated'}, domain=[('function_type','=','formulated')]),
        'is_corrosive': fields.boolean(string='Is Corrosive?', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'inert_quantity': fields.float(string='Inert Quantity', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'inert_quantity_uom': fields.many2one('product.uom', string='Inert Quantity UOM', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'commecial_product_rate_uom': fields.many2one('product.uom', string='Commercial Product Rate UOM', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'active_ingredient_rate_uom': fields.many2one('product.uom', string='Active Ingredient Rate UOM', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'mode_of_action': fields.text(string='Mode of Action', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'state': fields.selection(_states_, "State"),
        'environmental_class_id': fields.many2one('sgr.environmental_class', string='Environmental Class', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
        'emergency_information_id': fields.many2one('sgr.emergency_information', string='Emergency Information', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
        'toxicological_class_id': fields.many2one('sgr.toxicological_class', string='Toxicological Class', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
        'agronomic_class_id': fields.many2one('sgr.agronomic_class', string='Agronomic Class', readonly=True, required=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
        'partner_role_in_registry_ids': fields.one2many('sgr.partner_role_in_registry', 'formulated_product_registry_id', string='Partners Roles', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
        'physical_state_id': fields.many2one('sgr.physical_state', string='Phyisical State', readonly=True, required=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
        'packaging_ids': fields.one2many('sgr.packaging', 'formulated_product_registry_id', string='Packagings', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
        'techincal_product_ids': fields.many2many('product.product', 'sgr_formulated_product_registry_id_techincal_product_ids_rel', 'formulated_product_registry_id', 'product_id', string='Technical Products', states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}, context={'default_function_type':'technical'}, domain=[('function_type','=','technical')]), 
        'cqq_ids': fields.one2many('sgr.cqq', 'formulated_product_registry_id', string='CQQ', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
        'formulation_type_id': fields.many2one('sgr.formulation_type', string='Formulation Type', readonly=True, required=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
        'state_registry_ids': fields.one2many('sgr.state_registry', 'federal_registry_id', string='State Registries'), 
        'operated_by_ids': fields.one2many('sgr.formulated_product_registry', 'operate_id', string='Modified By', readonly=True), 
        'operate_id': fields.many2one('sgr.formulated_product_registry', string='Modify'), 
        'product_in_ret_ids': fields.many2many('sgr.product_in_ret', 'sgr_product_in_ret_ids_fromulated_product_registry_ids_rel', 'formulated_product_registry_id', 'product_in_ret_id', string='Used RETs', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
        'use_recommendation_ids': fields.one2many('sgr.use_recommendation', 'formulated_product_registry_id', string='Use Recommendations', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
        'component_registry_detail_ids': fields.many2many('sgr.component_registry_detail', 'sgr_component_registry_detail_ids_uses_ids_rel', 'formulated_product_registry_id', 'component_registry_detail_id', string='Component Registries', help=u"""Se debería dejar elegir solo component_Registr_detail donde exista algun formulated_product_ids igual al formulated_product de formulated product_Registry"""), 
    }

    _defaults = {
        'operation': 'new',
    }

    _order = "id desc"

    _constraints = [
    ]


    def get_mode_of_action(self, cr, uid, ids, context=None):
        """"""
        raise NotImplementedError

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
            wf_service.trg_delete(uid, 'sgr.formulated_product_registry', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.formulated_product_registry', obj_id, cr)
        return True

    def unlink(self, cr, uid, ids, context=None):
        sgr_registry_obj = self.pool.get('sgr.registry')
        data = self.read(cr, uid, ids, [ 'sgr_registry_id', ])
        res = super(formulated_product_registry, self).unlink(cr, uid, ids, context=context)
        for item in data:
            sgr_registry_obj.unlink(cr, uid, item['sgr_registry_id'][0],context=context)
        return res


formulated_product_registry()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
