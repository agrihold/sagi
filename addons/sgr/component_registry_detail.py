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

class component_registry_detail(osv.osv):
    """"""
    
    _name = 'sgr.component_registry_detail'
    _description = 'component_registry_detail'

    _columns = {
        'component_id': fields.many2one('product.product', string='Component', help=u"""Filtrar por productos del tipo component""", required=True, context={'default_function_type':'component'}, domain=[('function_type','=','component')]),
        'component_registry_id': fields.many2one('sgr.component_registry', string='Registry', ondelete='cascade', required=True), 
        'component_registry_finality_ids': fields.many2many('sgr.component_registry_finality', 'sgr___component_registry_finality_ids_rel', 'component_registry_detail_id', 'component_registry_finality_id', string='Finality', required=True), 
        'formulated_product_ids': fields.many2many('product.product', 'sgr_formulated_product_ids___rel', 'component_registry_detail_id', 'product_id', string='Formulated Products', context={'default_function_type':'formulated'}, domain=[('function_type','=','formulated')], required=True), 
        'uses_ids': fields.many2many('sgr.formulated_product_registry', 'sgr_component_registry_detail_ids_uses_ids_rel', 'component_registry_detail_id', 'formulated_product_registry_id', string='Uses', readonly=True), 
        'supplier_ids': fields.many2many('res.partner', 'sgr___supplier_ids_rel', 'component_registry_detail_id', 'partner_id', string='Suppliers', context={'default_supplier':'True','default_is_company':'True'}, domain=[('supplier','=',True)]), 
        'emergency_information_id': fields.many2one('sgr.emergency_information', string='Emergency Information'), 
        'cqq_ids': fields.one2many('sgr.cqq', 'component_registry_detail_id', string='CQQ'), 
        'packaging_ids': fields.one2many('sgr.packaging', 'component_registry_detail_id', string='Packaging'), 
    }

    _defaults = {
        'component_registry_id': lambda self, cr, uid, context=None: context and context.get('component_registry_id', False),
    }


    _constraints = [
    ]




component_registry_detail()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
