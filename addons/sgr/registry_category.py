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

class registry_category(osv.osv):
    """"""
    
    _name = 'sgr.registry_category'
    _description = 'registry_category'

    _columns = {
        'type': fields.selection([(u'state', u'State'), (u'laboratory', u'Laboratory'), (u'component', u'Component'), (u'ret', u'RET'), (u'technical_product', u'Technical Product'), (u'formulated_product', u'Formulated Product'), (u'trademark', u'Trademark')], string='Type', required=True),
        'name': fields.char(string='Name', required=True),
        'company_id': fields.many2one('res.company', string='Company', required=True),
        'registry_id': fields.one2many('sgr.registry', 'registry_category_id', string='&lt;no label&gt;'), 
        'information_category_ids': fields.many2many('sgr.information_category', 'sgr_registry_category_ids_information_category_ids_rel', 'registry_category_id', 'information_category_id', string='Information Categories', domain=[('hierachical_type','=','normal')]), 
        'document_category_ids': fields.many2many('sgr.document_category', 'sgr_registry_category_ids_document_category_ids_rel', 'registry_category_id', 'document_category_id', string='Document Categories'), 
        'goverment_agency_ids': fields.many2many('res.partner', 'sgr_registry_category_ids_goverment_agency_ids_rel', 'registry_category_id', 'partner_id', string='Processes', domain=[('is_gov_agency','=','True')]), 
        'registry_id': fields.many2many('sgr.registry', 'sgr_information_category_ids___rel', 'registry_category_id', 'registry_id', string='&lt;no label&gt;'), 
    }

    _defaults = {
        'company_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.registry_category', context=c),
    }


    _constraints = [
    ]




registry_category()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
