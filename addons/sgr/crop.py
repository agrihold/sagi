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

class crop(osv.osv):
    """"""
    
    _name = 'sgr.crop'
    _description = 'crop'

    _columns = {
        'name': fields.char(string='Scientific Name', required=True, size=32),
        'common_name': fields.char(string='Common Name', required=True, size=32, translate=True),
        'experimental_result_ids': fields.one2many('sgr.experimental_result', 'crop_id', string='experimental_result_ids'), 
        'state_registry_restriction_id': fields.one2many('sgr.state_registry_restriction', 'crop_id', string='&lt;no label&gt;'), 
        'ret_registry_ids': fields.many2many('sgr.ret_registry', 'sgr_ret_registry_ids_crop_ids_rel', 'crop_id', 'ret_registry_id', string='ret_registry_ids'), 
        'use_recommendation_id': fields.one2many('sgr.use_recommendation', 'crop_id', string='&lt;no label&gt;'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




crop()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
