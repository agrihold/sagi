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

from openerp.osv import osv

class laboratory_registry(osv.osv):
    """"""

    _name = 'sgr.laboratory_registry'
    _inherit = 'sgr.laboratory_registry'
    
    _rec_name = 'computed_name'

    def name_get(self, cr, uid, ids, context=None):
        if isinstance(ids, (list, tuple)) and not len(ids):
            return []
        if isinstance(ids, (long, int)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['laboratory_id','registry_category_id','operative_id'], context=context)
        res = []
        for record in reads:
            name = record['laboratory_id'][1]
            if record['registry_category_id']:
                name = record['registry_category_id'][1]+' - '+name
                if record['operative_id']:
                    name = record['operative_id'][1]+' - '+name
            res.append((record['id'], name))
        return res
    
    def create(self, cr, uid, vals, context=None):
        ids = super(laboratory_registry, self).create(cr, uid, vals, context=context)
        super(laboratory_registry, self).write(cr, uid, ids, {}, context=context)
        return ids
        
    def write(self, cr, uid, ids, vals, context=None):
        if not context:
            context = {}
        
        ret = super(laboratory_registry, self).write(cr, uid, ids, vals, context=context)
        if 'sgrx_from_computed_name' not in context or not context['sgrx_from_computed_name']:
            new_context = context.copy()
            new_context['sgrx_from_computed_name'] = True
            names = self.name_get(cr, uid, ids, context=context)
            for name in names:
                self.write(cr, uid, name[0], {'computed_name': name[1]}, context=new_context)
        
        return ret

laboratory_registry()
