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

class registry_process(osv.osv):
    """Son las presentaciones que se deben hacer para conseguir el registro. Cada presentación debebe tener un organizmo gubernamental definido"""
    
    _name = 'sgr.registry_process'
    _description = 'Son las presentaciones que se deben hacer para conseguir el regi'
    _inherits = {  }
    _inherit = [ 'mail.thread' ]

    _states_ = [
        # State machine: registry_process
        ('draft','Draft'),
        ('requested','Requested'),
        ('approved','Approved'),
        ('depreciated','Depreciated'),
        ('rejected','Rejected'),
        ('cancelled','Cancelled'),
    ]
    _track = {
        'state': {
            'sgr.registry_process_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.registry_process_requested': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'requested',
            'sgr.registry_process_approved': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'approved',
            'sgr.registry_process_depreciated': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'depreciated',
            'sgr.registry_process_rejected': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'rejected',
            'sgr.registry_process_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
        },
    }
    _columns = {
        'name': fields.char(string='Number', size=64),
        'petitioning_number': fields.char(string='Petitioning Number', size=64),
        'government_agency_id': fields.many2one('res.partner', string='Government Agency', required=True, context={'default_is_gov_agency':'True','default_is_company':'True'}, domain=[('is_gov_agency','=',True)]),
        'open_official_letter_id': fields.many2one('sgr.official_letter', string='Open Official Letter'),
        'close_official_letter_id': fields.many2one('sgr.official_letter', string='Close Oficial Letter'),
        'open_date': fields.date(string='Open Date'),
        'expected_date': fields.date(string='Expected Date'),
        'close_date': fields.date(string='Close Date'),
        'label_expected_date': fields.date(string='Label Expected Date'),
        'label_approval_date': fields.date(string='Label Approval Date'),
        'state': fields.selection(_states_, "State"),
        'registry_id': fields.many2one('sgr.registry', string='registry_id', ondelete='cascade', required=True), 
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
            wf_service.trg_delete(uid, 'sgr.registry_process', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.registry_process', obj_id, cr)
        return True



registry_process()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
