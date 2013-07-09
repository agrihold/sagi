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

class mode_of_action(osv.osv):
    """"""
    
    _name = 'sgr.mode_of_action'
    _description = 'mode_of_action'

    _columns = {
        'name': fields.char(string='Name', required=True, size=32, translate=True),
        'ingredient_ids': fields.many2many('sgr.ingredient', 'sgr_mode_of_action_ids_ingredient_ids_rel', 'mode_of_action_id', 'ingredient_id', string='ingredient_ids'), 
        'technical_product_registry_id': fields.many2many('sgr.technical_product_registry', 'sgr_technical_product_registry_id_mode_of_action_ids_rel', 'mode_of_action_id', 'technical_product_registry_id', string='technical_product_registry_id'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




mode_of_action()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
