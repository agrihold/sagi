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

class partner_role_in_registry(osv.osv):
    """"""
    
    _name = 'sgr.partner_role_in_registry'
    _description = 'partner_role_in_registry'

    _columns = {
        'partner_id': fields.many2one('res.partner', string='Partner', required=True),
        'type': fields.selection([(u'manufacturer', u'Manufacturer'), (u'formulator', u'Formulator'), (u'manipulator', u'Manipulator'), (u'importer', u'Importer'), (u'requestor', u'Requestor')], string='Type'),
        'formulated_product_registry_id': fields.many2one('sgr.formulated_product_registry', string='formulated_product_registry_id'), 
        'technical_product_registry_id': fields.many2one('sgr.technical_product_registry', string='technical_product_registry_id'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




partner_role_in_registry()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
