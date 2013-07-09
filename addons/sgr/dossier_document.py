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

class dossier_document(osv.osv):
    """"""
    
    _name = 'sgr.dossier_document'
    _description = 'dossier_document'
    _inherits = { 'sgr.document':'sgr_document_id' }
    _inherit = [ 'mail.thread' ]

    _states_ = [
        # State machine: dossier_document
        ('draft','Draft'),
        ('approved','Approved'),
        ('depreciated','Depreciated'),
        ('cancelled','Cancelled'),
    ]
    _track = {
        'state': {
            'sgr.dossier_document_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.dossier_document_approved': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'approved',
            'sgr.dossier_document_depreciated': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'depreciated',
            'sgr.dossier_document_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
        },
    }
    _columns = {
        'sgr_document_id': fields.many2one('sgr.document', 'Documents', ondelete='cascade', required=True, help=u""""""),
        'state': fields.selection(_states_, "State"),
        'registry_id': fields.many2one('sgr.registry', string='Registry', required=True, ondelete='cascade'), 
        'communication_ids': fields.many2many('sgr.communication', 'sgr_dossier_document_ids_communication_ids_rel', 'dossier_document_id', 'communication_id', string='Communications', readonly=True), 
    }

    _defaults = {
        'state': 'draft',
    }

    _order = "id desc"

    _constraints = [
    ]


    def get_default_company(self, cr, uid, ids, context=None):
        """"""
        member = getattr(self.pool.get('sgr.document'), 'get_default_company')
        return member(cr, uid, ids)

    def do_approve(self, cr, uid, ids, context=None):
        """"""
        member = getattr(self.pool.get('sgr.document'), 'do_approve')
        return member(cr, uid, ids)

    def do_depreciate(self, cr, uid, ids, context=None):
        """"""
        member = getattr(self.pool.get('sgr.document'), 'do_depreciate')
        return member(cr, uid, ids)

    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.dossier_document', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.dossier_document', obj_id, cr)
        return True

    def unlink(self, cr, uid, ids, context=None):
        sgr_document_obj = self.pool.get('sgr.document')
        data = self.read(cr, uid, ids, [ 'sgr_document_id', ])
        res = super(dossier_document, self).unlink(cr, uid, ids, context=context)
        for item in data:
            sgr_document_obj.unlink(cr, uid, item['sgr_document_id'][0],context=context)
        return res


dossier_document()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
