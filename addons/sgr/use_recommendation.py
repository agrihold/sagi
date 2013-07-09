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

class use_recommendation(osv.osv):
    """"""
    
    _name = 'sgr.use_recommendation'
    _description = 'use_recommendation'

    _columns = {
        'commecial_product_rate': fields.char(string='Commercial Product Rate', size=32),
        'active_ingredient_rate': fields.char(string='Active Ingredient Rate', size=32),
        'solution_volume': fields.char(string='Solution Volume', size=32),
        'solution_volume_uom': fields.many2one('product.uom', string='Solution Volume UOM'),
        'security_interval_in_days': fields.integer(string='Security Interval (Days)'),
        'application_time': fields.text(string='Application Time'),
        'LMR': fields.text(string='LMR'),
        'application_mode_id': fields.many2one('sgr.application_mode', string='Application Mode'), 
        'crop_id': fields.many2one('sgr.crop', string='Crop', required=True), 
        'tarjet_pest_id': fields.many2one('sgr.target_pests', string='Tarjet Pest', required=True), 
        'formulated_product_registry_id': fields.many2one('sgr.formulated_product_registry', string='formulated_product_registry_id', ondelete='cascade'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




use_recommendation()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
