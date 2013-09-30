# -*- coding: utf-8 -*-
##############################################################################
#
#    SGR. Sistema de Gestion de Registros
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

class registry(osv.osv):
    _name = 'sgr.registry'
    _inherit = [ _name ]
    
    _rec_name = 'computed_name'
    
    _columns = {
        'computed_name': fields.char(string='Name', size=256),
    }

    def create(self, cr, uid, vals, context=None):
        ids = super(registry, self).create(cr, uid, vals, context=context)
        super(registry, self).write(cr, uid, ids, {}, context=context)
        return ids
        
    def write(self, cr, uid, ids, vals, context=None):
        if not context:
            context = {}
        
        ret = super(registry, self).write(cr, uid, ids, vals, context=context)
        if 'sgrx_from_computed_name' not in context or not context['sgrx_from_computed_name']:
            new_context = context.copy()
            new_context['sgrx_from_computed_name'] = True
            for reg in self.browse(cr, uid, ids, context=context):
                if not reg.computed_name:
                    self.write(cr, uid, reg.id, {'computed_name': str(reg.id) + ', sgr.registry'}, context=new_context)
        
        return ret

    def onchange_registry_category(self, cr, uid, ids, registry_category_id, context=None):
        context = context or {}
        v = {}
        if registry_category_id:
            category_obj = self.pool.get('sgr.registry_category')
            category = category_obj.browse(cr, uid, registry_category_id)
            reg_id = False
            v['information_presentation_ids'] = [
                (0,0,{'information_category_id': inf.id,
                      'registry_id': reg_id})
                for inf in category.information_category_ids
            ]
            doc_categories = category.document_category_ids
            v['study_presentation_ids'] = [
                (0,0,{'document_category_id': doc.id,
                      'registry_id': reg_id})
                for doc in doc_categories
                if doc.type == 'study']
            v['partner_document_presentation_ids'] = [
                (0,0,{'document_category_id': doc.id,
                      'registry_id': reg_id})
                for doc in doc_categories
                if doc.type == 'partner_document']
            v['tax_ids'] = [
                (0,0,{'name': doc.name,
                      'document_category_id': doc.id,
                      'registry_id': reg_id})
                for doc in doc_categories
                if doc.type == 'tax']
            v['dossier_document_ids'] = [
                (0,0,{'name': doc.name,
                      'document_category_id': doc.id,
                      'registry_id': reg_id})
                for doc in doc_categories
                if doc.type == 'dossier_document']
            v['registry_process_ids'] = [
                (0,0,{'name': '',
                      'government_agency_id': gov.id,
                      'registry_id': reg_id})
                for gov in category.goverment_agency_ids]

        return {'value': v}

registry()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
