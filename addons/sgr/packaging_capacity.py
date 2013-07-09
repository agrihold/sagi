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

class packaging_capacity(osv.osv):
    """"""
    
    _name = 'sgr.packaging_capacity'
    _description = 'packaging_capacity'

    _columns = {
        'name': fields.float(string='Quantity', required=True),
        'uom_id': fields.many2one('product.uom', string='UOM', required=True),
        'packaging_ids': fields.many2many('sgr.packaging', 'sgr_packaging_capacity_ids_packaging_ids_rel', 'packaging_capacity_id', 'packaging_id', string='packaging_ids'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




packaging_capacity()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
