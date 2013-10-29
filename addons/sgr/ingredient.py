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

class ingredient(osv.osv):
    """"""
    
    _name = 'sgr.ingredient'
    _description = 'ingredient'

    _columns = {
        'type': fields.selection([(u'chemical', u'Active Chemical'), (u'biological', u'Active Biological'), (u'others', u'Others'), (u'impurity', u'Impurity')], string='Ingredient Type', required=True),
        'common_international_name': fields.char(string='Common International Name', size=128),
        'name': fields.char(string='Common Name', required=True, size=64, translate=True),
        'scientific_name': fields.char(string='IUPAC/Scientific Name', size=128),
        'cas': fields.char(string='CAS Number', size=32),
        'molecular_formula': fields.char(string='Molecular Formula', size=32),
        'chemical_structure': fields.binary(string='Chemical Structure'),
        'molecular_weight': fields.float(string='Molecular Weight'),
        'mol_weight_uom_id': fields.many2one('product.uom', string='Molecular Weight UOM'),
        'density': fields.float(string='Density'),
        'density_uom_id': fields.many2one('product.uom', string='Density UOM'),
        'solubility': fields.float(string='Solubility'),
        'solubility_uom_id': fields.many2one('product.uom', string='Solubility UOM'),
        'synonymy': fields.char(string='Synonymy', size=256),
        'note': fields.text(string='Note'),
        'ingredient_group_id': fields.many2one('sgr.ingredient_group', string='Ingredient Group', required=True), 
        'agronomic_class_id': fields.many2one('sgr.agronomic_class', string='Agronomic Class'), 
        'cqq_ids': fields.one2many('sgr.cqq', 'ingredient_id', string='cqq_ids'), 
        'cqq_id': fields.many2many('sgr.cqq', 'sgr___scientific_name_rel', 'ingredient_id', 'cqq_id', string='&lt;no label&gt;'), 
        'ingredient_other_name_ids': fields.one2many('sgr.ingredient_other_name', 'ingredient_id', string='Ingredient Others Names'), 
        'mode_of_action_ids': fields.many2many('sgr.mode_of_action', 'sgr_mode_of_action_ids_ingredient_ids_rel', 'ingredient_id', 'mode_of_action_id', string='Modes Of Action'), 
        'lmr_ids': fields.one2many('sgr.lmr', 'ingredient_id', string='LMR'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




ingredient()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
