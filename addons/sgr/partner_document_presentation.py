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

class partner_document_presentation(osv.osv):
    """"""
    
    _name = 'sgr.partner_document_presentation'
    _description = 'partner_document_presentation'

    _states_ = [
        # State machine: partner_document_presentation
        ('draft','Draft'),
        ('approved','Approved'),
        ('cancelled','Cancelled'),
    ]
    _columns = {
        'state': fields.selection(_states_, "State"),
        'registry_id': fields.many2one('sgr.registry', string='registry_id', ondelete='cascade', required=True), 
        'document_category_id': fields.many2one('sgr.document_category', string='Category', readonly=True, required=True, states={'draft': [('readonly', False)]}, domain=[('hierachical_type','=','normal')]), 
        'partner_document_id': fields.many2one('sgr.partner_document', string='Partner Document', readonly=True, states={'draft': [('readonly', False)]}), 
        'communication_ids': fields.many2many('sgr.communication', 'sgr_communication_ids_partner_document_presentation_ids_rel', 'partner_document_presentation_id', 'communication_id', string='Communications', readonly=True), 
    }

    _defaults = {
        'state': 'draft',
    }


    _constraints = [
    ]


    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.partner_document_presentation', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.partner_document_presentation', obj_id, cr)
        return True



partner_document_presentation()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
