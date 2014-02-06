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
import netsvc
from osv import osv, fields

class study(osv.osv):
    """"""
    
    _name = 'sgr.study'
    _inherit = [ _name ]

    _columns = {
        'document_category_show_validation_method': fields.related('document_category_id', 'show_validation_method', type='boolean', string='Show validation method'),
        'document_category_experimental_results': fields.related('document_category_id', 'experimental_results', type='char', string='Experimental Results'),
    }

    def name_get(self, cr, uid, ids, context=None):
        # always return the full hierarchical name
        res = {}
        for line in self.browse(cr, uid, ids):
            if line.name and line.reference:
                sep = ' - '
            else:
                sep = ''
            res[line.id] = (line.name or '')+ sep + (line.reference or '')
        return res.items()     

    def name_search(self, cr, user, name='', args=None, operator='ilike', context=None, limit=100):
        if not args:
            args = []    
        ids = set()     
        if name:
            ids.update(self.search(cr, user, args + [('name',operator,name)], limit=(limit and (limit-len(ids)) or False) , context=context))
            if not limit or len(ids) < limit:
                ids.update(self.search(cr, user, args + [('reference',operator,name)], limit=limit, context=context))
            ids = list(ids)
        else:
            ids = self.search(cr, user, args, limit=limit, context=context)
        result = self.name_get(cr, user, ids, context=context)
        return result
        
    def onchange_document_category(self, cr, uid, ids, document_category_id, context=None):
        v = {}
        
        if document_category_id:
            document_category_obj = self.pool.get('sgr.document_category')
            document_category = document_category_obj.browse(cr, uid, document_category_id, context=context)
            
            if not document_category:
                return {'value': v}
            
            if isinstance(document_category, list):
                document_category = document_category[0]
            v['document_category_show_validation_method'] = document_category.show_validation_method
            v['document_category_experimiental_results'] = document_category.experimiental_results
        else:
            v['document_category_show_validation_method'] = False
            v['document_category_experimiental_results'] = 'oerp_default'       
        
        return {'value': v}
    
study()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
