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

from openerp.osv import osv,fields

class formulated_product_registry(osv.osv):
    """"""

    _name = 'sgr.formulated_product_registry'
    _inherit = 'sgr.formulated_product_registry'    
    _rec_name = 'computed_name'

    _columns = {
        'number': fields.integer(string='Number', readonly=True),
    }

    _defaults = {
        'number': 1,
    }

    def name_get(self, cr, uid, ids, context=None):
        if isinstance(ids, (list, tuple)) and not len(ids):
            return []
        if isinstance(ids, (long, int)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['formulated_product_id','registry_category_id','operative_id'], context=context)
        res = []
        for record in reads:
            name = record['formulated_product_id'][1]
            if record['registry_category_id']:
                name = record['registry_category_id'][1]+' - '+name
                if record['operative_id']:
                    name = record['operative_id'][1]+' - '+name
            res.append((record['id'], name))
        return res
    
    def create(self, cr, uid, vals, context=None):
        ids = super(formulated_product_registry, self).create(cr, uid, vals, context=context)
        super(formulated_product_registry, self).write(cr, uid, ids, {}, context=context)
        return ids
        
    def write(self, cr, uid, ids, vals, context=None):
        if not context:
            context = {}
        
        ret = super(formulated_product_registry, self).write(cr, uid, ids, vals, context=context)
        if 'sgrx_from_computed_name' not in context or not context['sgrx_from_computed_name']:
            new_context = context.copy()
            new_context['sgrx_from_computed_name'] = True
            names = self.name_get(cr, uid, ids, context=context)
            for name in names:
                self.write(cr, uid, name[0], {'computed_name': name[1]}, context=new_context)
        
        return ret

formulated_product_registry()
