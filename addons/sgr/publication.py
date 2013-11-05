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

class publication(osv.osv):
    """"""
    
    _name = 'sgr.publication'
    _description = 'publication'

    _columns = {
        'name': fields.char(string='Name', required=True, size=64),
        'number': fields.char(string='Number', size=32),
        'published_on_page': fields.char(string='Published on Page', size=32),
        'publication_date': fields.date(string='Publication Date', required=True),
        'act_date': fields.date(string='Act Date'),
        'act': fields.char(string='Act', size=32),
        'description': fields.text(string='Description'),
        'company_id': fields.many2one('res.company', string='Company', readonly=True, required=True),
        'registry_id': fields.many2one('sgr.registry', string='registry_id', ondelete='cascade', required=True), 
        'publication_type_id': fields.many2one('sgr.publication_type', string='Type', required=True), 
    }

    _defaults = {
        'company_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.publication', context=c),
    }


    _constraints = [
    ]




publication()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
