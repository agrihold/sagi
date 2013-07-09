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

class partner_document(osv.osv):
    """"""
    
    _name = 'sgr.partner_document'
    _description = 'partner_document'
    _inherits = { 'sgr.document':'sgr_document_id' }
    _inherit = [ 'mail.thread' ]

    _states_ = [
        # State machine: untitle
        ('draft','Draft'),
        ('approved','Approved'),
        ('cancelled','Cancelled'),
        ('depreciated','Depreciated'),
    ]
    _track = {
        'state': {
            'sgr.partner_document_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.partner_document_approved': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'approved',
            'sgr.partner_document_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
            'sgr.partner_document_depreciated': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'depreciated',
        },
    }
    _columns = {
        'sgr_document_id': fields.many2one('sgr.document', 'Documents', ondelete='cascade', required=True, help=u""""""),
        'partner_id': fields.many2one('res.partner', string='Partner', required=True),
        'state': fields.selection(_states_, "State"),
        'partner_document_presentation_ids': fields.one2many('sgr.partner_document_presentation', 'partner_document_id', string='Presentations', readonly=True), 
        'replace_ids': fields.one2many('sgr.partner_document', 'replaced_by_id', string='Replacing'), 
        'replaced_by_id': fields.many2one('sgr.partner_document', string='Replaced By'), 
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

    def action_wfk_set_cancelled(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'cancelled'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.partner_document', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.partner_document', obj_id, cr)
        return True

    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.partner_document', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.partner_document', obj_id, cr)
        return True

    def unlink(self, cr, uid, ids, context=None):
        sgr_document_obj = self.pool.get('sgr.document')
        data = self.read(cr, uid, ids, [ 'sgr_document_id', ])
        res = super(partner_document, self).unlink(cr, uid, ids, context=context)
        for item in data:
            sgr_document_obj.unlink(cr, uid, item['sgr_document_id'][0],context=context)
        return res


partner_document()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
