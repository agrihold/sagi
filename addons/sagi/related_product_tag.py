# -*- coding: utf-8 -*-
##############################################################################
#
#    SAGI
#    Copyright (C) 2013 No author.
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

class related_product_tag(osv.osv):
    """"""
    
    _name = 'sagi.related_product_tag'
    _description = 'related_product_tag'

    _columns = {
        'name': fields.char(string='Name', required=True, size=32),
        'related_product_id': fields.many2many('sagi.related_product', 'sagi___related_product_tag_ids_rel', 'related_product_tag_id', 'related_product_id', string='&lt;no label&gt;'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




related_product_tag()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
