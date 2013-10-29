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

class experimental_result(osv.osv):
    """"""
    
    _name = 'sgr.experimental_result'
    _description = 'experimental_result'

    _columns = {
        'city': fields.char(string='City', size=32),
        'volume': fields.float(string='Volume'),
        'volume_uom_id': fields.many2one('product.uom', string='Volume UOM'),
        'doses': fields.char(string='Doses', size=64),
        'doses_uom_id': fields.many2one('product.uom', string='Doses UOM'),
        'number_of_applications': fields.integer(string='Number of Applications'),
        'result': fields.char(string='Result', size=128),
        'note': fields.text(string='Note'),
        'study_experimental_results': fields.char(string='Experimental Results', size=16),
        'study_id': fields.many2one('sgr.study', string='study_id', ondelete='cascade', required=True), 
        'crop_id': fields.many2one('sgr.crop', string='Crops', required=True), 
        'target_pest_id': fields.many2one('sgr.target_pests', string='Target Pests', required=True), 
    }

    _defaults = {
    }


    _constraints = [
    ]




experimental_result()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
