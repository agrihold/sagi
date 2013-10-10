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

class component_registry_finality(osv.osv):
    """"""
    
    _name = 'sgr.component_registry_finality'
    _description = 'component_registry_finality'

    _columns = {
        'name': fields.char(string='Name', required=True, size=64),
        'component_registry_detail_id': fields.many2many('sgr.component_registry_detail', 'sgr___component_registry_finality_ids_rel', 'component_registry_finality_id', 'component_registry_detail_id', string='&lt;no label&gt;'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




component_registry_finality()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
