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

class status_report(osv.osv):
    """"""
    
    _name = 'sagi.status_report'
    _description = 'status_report'

    _columns = {
        'date': fields.date(string='Date', required=True),
        'report': fields.binary(string='Report', required=True),
        'new_product_project_id': fields.many2one('sagi.new_product_project', string='&lt;no label&gt;', ondelete='cascade', required=True), 
    }

    _defaults = {
    }


    _constraints = [
    ]




status_report()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
