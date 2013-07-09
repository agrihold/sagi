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

class npp_excecution(osv.osv):
    """"""
    
    _name = 'sagi.new_product_project'
    _inherits = {  }
    _inherit = [ 'sagi.new_product_project' ]

    _track = {
    }
    _columns = {
        'excecution_date_to_start': fields.date(string='Date to Start'),
        'excecution_date_to_end': fields.date(string='Date to End'),
        'excecution_started_date': fields.date(string='Started Date'),
        'excecution_end_date': fields.date(string='End Date'),
        'kick_off_project_file': fields.binary(string='Project Kick Off'),
    }

    _defaults = {
    }


    _constraints = [
    ]




npp_excecution()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
