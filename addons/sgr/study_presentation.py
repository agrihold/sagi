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

class study_presentation(osv.osv):
    """"""
    
    _name = 'sgr.study_presentation'
    _description = 'study_presentation'

    _states_ = [
        # State machine: study_presentation
        ('draft','draft'),
        ('approved','approved'),
        ('cancelled','cancelled'),
    ]
    _columns = {
        'state': fields.selection(_states_, "State"),
        'study_id': fields.many2one('sgr.study', string='Study', readonly=True, states={'draft': [('readonly', False)]}), 
        'document_category_id': fields.many2one('sgr.document_category', string='Category', readonly=True, required=True, states={'draft': [('readonly', False)]}, domain=[('hierachical_type','=','normal')]), 
        'registry_id': fields.many2one('sgr.registry', string='registry_id', ondelete='cascade', required=True), 
        'communication_ids': fields.many2many('sgr.communication', 'sgr_study_presentation_ids_communication_ids_rel', 'study_presentation_id', 'communication_id', string='Communications', readonly=True), 
    }

    _defaults = {
        'state': 'draft',
    }


    _constraints = [
    ]


    def action_wfk_set_cancelled(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'cancelled'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.study_presentation', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.study_presentation', obj_id, cr)
        return True

    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.study_presentation', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.study_presentation', obj_id, cr)
        return True



study_presentation()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
