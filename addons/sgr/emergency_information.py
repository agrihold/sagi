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

class emergency_information(osv.osv):
    """"""
    
    _name = 'sgr.emergency_information'
    _description = 'emergency_information'

    _columns = {
        'name': fields.char(string='Name', required=True, size=32, translate=True),
        'formulated_product_registry_id': fields.one2many('sgr.formulated_product_registry', 'emergency_information_id', string='formulated_product_registry_id'), 
        'technical_product_registry_id': fields.one2many('sgr.technical_product_registry', 'emergency_information_id', string='technical_product_registry_id'), 
        'component_registry_detail_id': fields.one2many('sgr.component_registry_detail', 'emergency_information_id', string='&lt;no label&gt;'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




emergency_information()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
