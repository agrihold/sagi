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

class communication(osv.osv):
    """"""
    
    _name = 'sgr.communication'
    _description = 'communication'
    _inherits = {  }
    _inherit = [ 'mail.thread' ]

    _states_ = [
        # State machine: communication
        ('draft','Draft'),
        ('sent','Sent'),
        ('received','Received'),
        ('resolving_request','Resolving Request'),
        ('resolved','Resolved'),
        ('cancelled','Cancelled'),
    ]
    _track = {
        'state': {
            'sgr.communication_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.communication_sent': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'sent',
            'sgr.communication_received': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'received',
            'sgr.communication_resolving_request': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'resolving_request',
            'sgr.communication_resolved': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'resolved',
            'sgr.communication_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
        },
    }
    _columns = {
        'date': fields.date(string='Date', readonly=True, states={'draft': [('readonly', False)]}),
        'direction': fields.selection([(u'in', u'In'), (u'out', u'Out')], string='Direction', readonly=True, required=True, states={'draft': [('readonly', False)]}),
        'name': fields.char(string='Name', readonly=True, required=True, size=128, states={'draft': [('readonly', False)]}),
        'government_agency_id': fields.many2one('res.partner', string='Government Agency', readonly=True, required=True, states={'draft': [('readonly', False)]}, context={'default_is_gov_agency':'True','default_is_company':'True'}, domain=[('is_gov_agency','=',True)]),
        'term_date': fields.date(string='Term Date', readonly=True, states={'draft': [('readonly', False)]}),
        'note': fields.html(string='Note'),
        'company_id': fields.many2one('res.company', string='Company', readonly=True, required=True),
        'state': fields.selection(_states_, "State"),
        'registry_id': fields.many2one('sgr.registry', string='Registry', ondelete='cascade', required=True), 
        'tax_ids': fields.many2many('sgr.tax', 'sgr_tax_ids_communication_ids_rel', 'communication_id', 'tax_id', string='Taxes'), 
        'dossier_document_ids': fields.many2many('sgr.dossier_document', 'sgr_dossier_document_ids_communication_ids_rel', 'communication_id', 'dossier_document_id', string='Dossier Documents'), 
        'study_presentation_ids': fields.many2many('sgr.study_presentation', 'sgr_study_presentation_ids_communication_ids_rel', 'communication_id', 'study_presentation_id', string='Studies'), 
        'official_letter_id': fields.many2one('sgr.official_letter', string='Official Letter'), 
        'communication_type_id': fields.many2one('sgr.communication_type', string='Type', readonly=True, states={'draft': [('readonly', False)]}, domain=[('hierachical_type','=','normal')], required=True), 
        'partner_document_presentation_ids': fields.many2many('sgr.partner_document_presentation', 'sgr_communication_ids_partner_document_presentation_ids_rel', 'communication_id', 'partner_document_presentation_id', string='Documents'), 
    }

    _defaults = {
        'state': 'draft',
        'company_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.communication', context=c),
        'study_presentation_ids': lambda self, cr, uid, context=None: context and context.get('study_presentation_ids', False),
        'partner_document_presentation_ids': lambda self, cr, uid, context=None: context and context.get('partner_document_presentation_ids', False),
    }

    _order = "id desc"

    _constraints = [
    ]


    def get_default_company(self, cr, uid, ids, context=None):
        """"""
        raise NotImplementedError

    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.communication', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.communication', obj_id, cr)
        return True



communication()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
