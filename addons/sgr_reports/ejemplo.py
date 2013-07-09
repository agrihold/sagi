# -*- coding: utf-8 -*-
##############################################################################
#
#    
#    Copyright (C) 2013 No author.
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


import netsvc
from osv import osv, fields

class sagi(osv.osv):
    """
        """
    _name = 'sagi.sagi'
    _description = 'sagi'
    _inherit = [ 'mail.thread' ]

    _columns = {
        'agronomic_class': fields.many2one('sgr.agronomic_class', 'Agronomic Class', required=True), 
        'create_date': fields.date('Create Date', readonly=True), 
        'created_by': fields.many2one('res.users', 'Created By', readonly=True), 
        'next_action': fields.char('next_action'), 
        'next_action_date': fields.date('next_action_date'), 
        'responsible': fields.many2one('res.users', 'responsible'), 
        'reference': fields.char('reference'), 
        'state': fields.selection([(u'on_creation', u'On Creation'), (u'on_initiation', u'On Initiation'), (u'on_planning', u'On Planning'), (u'on_excecution_and_control', u'On Excecution and Control'), (u'on_closure', u'On Closure'), (u'closed', u'Closed'), (u'rejected', u'Rejected'), (u'cancelled', u'Cancelled'), (u'aborted', u'Aborted'), (u'draft', u'Draft')], "State"),
        'sagi_stage_id': fields.one2many('sagi.sagi_stage', 'sagi_id', '<no label>'), 
    }

    _defaults = {
        'state': 'draft',
    }



    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sagi.sagi', obj_id, cr)
            wf_service.trg_create(uid, 'sagi.sagi', obj_id, cr)
        return True


sagi()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
