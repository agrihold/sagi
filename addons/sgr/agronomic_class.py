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

class agronomic_class(osv.osv):
    """"""
    
    _name = 'sgr.agronomic_class'
    _description = 'agronomic_class'

    _columns = {
        'name': fields.char(string='Name', required=True, size=32, translate=True),
        'ingredient_ids': fields.one2many('sgr.ingredient', 'agronomic_class_id', string='ingredient_ids'), 
        'technical_product_registry_id': fields.one2many('sgr.technical_product_registry', 'agronomic_class_id', string='technical_product_registry_id'), 
        'formulated_product_registry_ids': fields.one2many('sgr.formulated_product_registry', 'agronomic_class_id', string='formulated_product_registry_ids'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




agronomic_class()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
