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

class information_presentation(osv.osv):
    """"""
    
    _name = 'sgr.information_presentation'
    _description = 'information_presentation'

    _states_ = [
        # State machine: information_presentation
        ('draft','Draft'),
        ('approved','Approved'),
        ('cancelled','Cancelled'),
    ]
    _columns = {
        'text': fields.html(string='Text', readonly=True, states={'draft': [('readonly', False)]}, translate=True),
        'state': fields.selection(_states_, "State"),
        'registry_id': fields.many2one('sgr.registry', string='registry_id', ondelete='cascade', required=True), 
        'parent_information_id': fields.many2one('sgr.information', string='Information', readonly=True, states={'draft': [('readonly', False)]}), 
        'information_category_id': fields.many2one('sgr.information_category', string='Category', readonly=True, required=True, states={'draft': [('readonly', False)]}), 
    }

    _defaults = {
        'state': 'draft',
    }


    _constraints = [
    ]


    def onchange_parent_information(self, cr, uid, ids, parent_information_id, context=None):
        """analogo a los productos en una nota de venta. Cuando en un registor se agrega una informacion, se trae el texto de la misma que puede ser modificado por el usuario en esa informacion. A su vez puede existir una información en un registro sin tener asociada una información"""
        raise NotImplementedError

    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.information_presentation', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.information_presentation', obj_id, cr)
        return True



information_presentation()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
