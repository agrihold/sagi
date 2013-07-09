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

class document_category(osv.osv):
    """"""
    
    def name_get(self, cr, uid, ids, context=None):
        if isinstance(ids, (list, tuple)) and not len(ids):
            return []
        if isinstance(ids, (long, int)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name','parent_id'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['parent_id']:
                name = record['parent_id'][1]+' / '+name
            res.append((record['id'], name))
        return res

    def _name_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_get(cr, uid, ids, context=context)
        return dict(res)

    def _check_recursion(self, cr, uid, ids, context=None):
        level = 100
        while len(ids):
            cr.execute('select distinct parent_id from sgr_document_category where id IN %s',(tuple(ids),))
            ids = filter(None, map(lambda x:x[0], cr.fetchall()))
            if not level:
                return False
            level -= 1
        return True

    _name = 'sgr.document_category'
    _description = 'document_category'

    _columns = {
        'complete_name': fields.function(_name_get_fnc, type="char", string='Name', store=True),
        'type': fields.selection([(u'partner_document', u'Partner Document'), (u'study', u'Study'), (u'dossier_document', u'Dossier Document'), (u'tax', u'Tax')], string='Document Type', required=True),
        'name': fields.char(string='Name', required=True, size=64, translate=True),
        'hierachical_type': fields.selection([(u'view', u'View'), (u'normal', u'Normal')], string='Type', required=True),
        'company_id': fields.many2one('res.company', string='Company'),
        'experimental_results': fields.selection([(u'efficacy', u'Efficacy'), (u'residue', u'Residue')], string='Experimiental Results'),
        'show_validation_method': fields.boolean(string='Show validation method'),
        'reference': fields.char(string='Reference', size=32),
        'product_study_ids': fields.one2many('sgr.product_study', 'study_category_id', string='product_study_ids'), 
        'document_ids': fields.one2many('sgr.document', 'document_category_id', string='document_ids'), 
        'partner_document_presentation_ids': fields.one2many('sgr.partner_document_presentation', 'document_category_id', string='Doc. Presentation'), 
        'parent_id': fields.many2one('sgr.document_category', string='Parent Category'), 
        'child_ids': fields.one2many('sgr.document_category', 'parent_id', string='Child Categories'), 
        'registry_category_ids': fields.many2many('sgr.registry_category', 'sgr_registry_category_ids_document_category_ids_rel', 'document_category_id', 'registry_category_id', string='registry_category_ids'), 
        'study_presentation_ids': fields.one2many('sgr.study_presentation', 'document_category_id', string='study_presentation_ids'), 
    }

    _defaults = {
        'hierachical_type': 'normal',
        'company_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.document_category', context=c),
    }


    _constraints = [
        (_check_recursion, 'Error ! You cannot create recursive document_category.', ['parent_id'])
    ]


    def get_default_company(self, cr, uid, ids, context=None):
        """"""
        raise NotImplementedError



document_category()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
