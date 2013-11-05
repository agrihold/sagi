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

class ret_phase(osv.osv):
    """"""
    
    _name = 'sgr.ret_phase'
    _description = 'ret_phase'

    _columns = {
        'name': fields.char(string='Name', required=True, size=4, translate=True),
        'ret_registry_ids': fields.one2many('sgr.ret_registry', 'ret_phase_id', string='ret_registry_ids'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




ret_phase()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
