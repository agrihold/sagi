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

class npp_gantt_view(osv.osv):
    """"""
    
    _name = 'sagi.npp_gantt_view'
    _description = 'npp_gantt_view'

    _columns = {
        'name': fields.char(string='Name', size=32),
        'date_start': fields.date(string='date_start'),
        'date_stop': fields.date(string='date_stop'),
        'sequence': fields.integer(string='sequence'),
        'new_product_project_id': fields.many2one('sagi.new_product_project', string='new_product_project_id', ondelete='cascade', required=True), 
    }

    _defaults = {
    }


    _constraints = [
    ]




npp_gantt_view()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
