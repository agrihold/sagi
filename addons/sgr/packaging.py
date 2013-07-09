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

class packaging(osv.osv):
    """"""
    
    _name = 'sgr.packaging'
    _description = 'packaging'

    _columns = {
        'external_quantity': fields.integer(string='External Quantity'),
        'uom_id': fields.many2one('product.uom', string='UOM'),
        'technical_product_registry_id': fields.many2one('sgr.technical_product_registry', string='technical_product_registry_id'), 
        'internal_packaging_material_id': fields.many2one('sgr.packaging_material', string='Int. Material', required=True), 
        'external_packaging_material_id': fields.many2one('sgr.packaging_material', string='Ext. Material'), 
        'internal_packaging_type_id': fields.many2one('sgr.packaging_type', string='Int. Type', required=True), 
        'external_packaging_type_id': fields.many2one('sgr.packaging_type', string='Ext. Type'), 
        'formulated_product_registry_id': fields.many2one('sgr.formulated_product_registry', string='formulated_product_registry_id'), 
        'sample_request_id': fields.many2one('sgr.sample_request', string='sample_request_id'), 
        'packaging_capacity_ids': fields.many2many('sgr.packaging_capacity', 'sgr_packaging_capacity_ids_packaging_ids_rel', 'packaging_id', 'packaging_capacity_id', string='Capacity'), 
        'component_registry_detail_id': fields.many2one('sgr.component_registry_detail', string='component_registry_detail_id'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




packaging()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
