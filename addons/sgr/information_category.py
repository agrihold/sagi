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

class information_category(osv.osv):
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
            cr.execute('select distinct parent_id from sgr_information_category where id IN %s',(tuple(ids),))
            ids = filter(None, map(lambda x:x[0], cr.fetchall()))
            if not level:
                return False
            level -= 1
        return True

    _name = 'sgr.information_category'
    _description = 'information_category'

    _columns = {
        'complete_name': fields.function(_name_get_fnc, type="char", string='Name', store=True),
        'name': fields.char(string='Name', required=True, size=128),
        'hierachical_type': fields.selection([(u'view', u'View'), (u'normal', u'Normal')], string='Type', required=True),
        'header': fields.html(string='Header', translate=True),
        'footer': fields.html(string='Footer', translate=True),
        'company_id': fields.many2one('res.company', string='Company'),
        'registry_category_ids': fields.many2many('sgr.registry_category', 'sgr_registry_category_ids_information_category_ids_rel', 'information_category_id', 'registry_category_id', string='registry_category_ids'), 
        'information_ids': fields.one2many('sgr.information', 'information_category_id', string='information_ids'), 
        'child_ids': fields.one2many('sgr.information_category', 'parent_id', string='Child Categories'), 
        'parent_id': fields.many2one('sgr.information_category', string='Parent Category'), 
        'information_presentation_ids': fields.one2many('sgr.information_presentation', 'information_category_id', string='Inf. Presentation'), 
    }

    _defaults = {
        'hierachical_type': 'normal',
        'company_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.information_category', context=c),
    }


    _constraints = [
        (_check_recursion, 'Error ! You cannot create recursive information_category.', ['parent_id'])
    ]




information_category()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
