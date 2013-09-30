# -*- coding: utf-8 -*-
##############################################################################
#
#    SGR. Sistema de Gestion de Registros
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
import netsvc
from osv import osv, fields

class product(osv.osv):
    """"""
    _name = 'product.product'
    _inherits = {  }
    _inherit = [ 'product.product' ]

    _states_ = [
    ]

    _columns = {
        'technical_product_registry_ids': fields.one2many('sgr.technical_product_registry', 'technical_product_id', string='Registries'), 
        'product_in_ret_ids': fields.one2many('sgr.product_in_ret', 'product_id', string='RETs'), 
        'component_registry_detail_ids': fields.one2many('sgr.component_registry_detail', 'component_id', string='Registries'), 
        'formulated_product_registry_ids': fields.one2many('sgr.formulated_product_registry', 'formulated_product_id', string='Registries'),  
    }

    _defaults = {
    }


product()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
