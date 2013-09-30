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

class state_registry_restriction(osv.osv):
    """"""
    
    _name = 'sgr.state_registry_restriction'
    _description = 'state_registry_restriction'

    _columns = {
        'restriction': fields.text(string='Restriction'),
        'note': fields.text(string='Note'),
        'tarjet_pest_id': fields.many2one('sgr.target_pests', string='Tarjet Pest', required=True), 
        'crop_id': fields.many2one('sgr.crop', string='Crop', required=True), 
        'state_registry_id': fields.many2one('sgr.state_registry', string='state_registry_id', ondelete='cascade', required=True), 
    }

    _defaults = {
    }


    _constraints = [
    ]




state_registry_restriction()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
