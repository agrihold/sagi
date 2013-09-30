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

class study_method(osv.osv):
    """"""
    
    _name = 'sgr.study_method'
    _description = 'study_method'

    _columns = {
        'name': fields.char(string='Name', required=True, size=64, translate=True),
        'description': fields.text(string='Description', required=True, translate=True),
        'study_ids': fields.many2many('sgr.study', 'sgr_study_ids_study_method_ids_rel', 'study_method_id', 'study_id', string='study_ids'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




study_method()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
