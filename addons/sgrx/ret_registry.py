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

class ret_registry(osv.osv):
    """"""

    _name = 'sgr.ret_registry'
    _inherit = 'sgr.ret_registry'
    
    _rec_name = 'computed_name'

    def create(self, cr, uid, vals, context=None):
        ids = super(ret_registry, self).create(cr, uid, vals, context=context)
        super(ret_registry, self).write(cr, uid, ids, {}, context=context)
        return ids
        
    def write(self, cr, uid, ids, vals, context=None):
        if not context:
            context = {}
        
        ret = super(ret_registry, self).write(cr, uid, ids, vals, context=context)
        if 'sgrx_from_computed_name' not in context or not context['sgrx_from_computed_name']:
            new_context = context.copy()
            new_context['sgrx_from_computed_name'] = True
            for registry in self.browse(cr, uid, ids, context=context):
                self.write(cr, uid, registry.id, {'computed_name': registry.name}, context=new_context)
        
        return ret

ret_registry()
