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

class cqq(osv.osv):
    """"""
    
    _name = 'sgr.cqq'
    _description = 'cqq'

    _columns = {
        'declared_concentration': fields.float(string='Declared Concentration', digits=(4,10)),
        'min_concentration': fields.float(string='Minimum Conc.', digits=(4,10)),
        'max_concentration': fields.float(string='Maximum Conc.', digits=(4,10)),
        'uom_id': fields.many2one('product.uom', string='UOM'),
        'min_uom_id': fields.many2one('product.uom', string='UOM'),
        'max_uom_id': fields.many2one('product.uom', string='UOM'),
        'main_ingredient': fields.boolean(string='Main Ing.'),
        'ingredient_function_id': fields.many2one('sgr.ingredient_function', string='Function', required=True), 
        'ingredient_id': fields.many2one('sgr.ingredient', string='Ingredient', required=True, ondelete='cascade'), 
        'technical_product_registry_id': fields.many2one('sgr.technical_product_registry', string='technical_product_registry_id'), 
        'formulated_product_registry_id': fields.many2one('sgr.formulated_product_registry', string='formulated_product_registry_id'), 
        'scientific_name': fields.related(
                    'ingredient_id',
                    'scientific_name',
                    type='char',
                    relation='sgr.ingredient',
                    string='IUPAC/Scientific Name', readonly=True
                    ),
        'component_registry_detail_id': fields.many2one('sgr.component_registry_detail', string='component_registry_detail_id'), 
    }

    _defaults = {
        'main_ingredient': True,
    }


    _constraints = [
    ]




cqq()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
