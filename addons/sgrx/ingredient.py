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

class ingredient(osv.osv):
    """"""

    _name = 'sgr.ingredient'
    _inherit = 'sgr.ingredient'

    #def name_get(self, cr, uid, ids, context=None):
        #if isinstance(ids, (list, tuple)) and not len(ids):
            #return []
        #if isinstance(ids, (long, int)):
            #ids = [ids]
        #reads = self.read(cr, uid, ids, ['name','common_name'], context=context)
        #res = []
        #for record in reads:
            #name = record['name'][1]
            #if record['registry_category_id']:
                #name = record['registry_category_id'][1]+' - '+name
                #if record['operative_id']:
                    #name = record['operative_id'][1]+' - '+name
            #res.append((record['id'], name))
        #return res
    def name_get(self, cr, uid, ids, context=None):
        if isinstance(ids, (list, tuple)) and not len(ids):
            return []
        if isinstance(ids, (long, int)): 
            ids = [ids]
        reads = self.read(cr, uid, ids, ['cas','name'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['cas']:
                name = record['cas']+' - '+name
            res.append((record['id'], name))
        return res
        
