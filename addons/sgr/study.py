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

class study(osv.osv):
    """"""
    
    _name = 'sgr.study'
    _description = 'study'
    _inherits = { 'sgr.document':'sgr_document_id' }
    _inherit = [ 'mail.thread','mail.thread' ]

    _states_ = [
        # State machine: study
        ('draft','Draft'),
        ('contracted','Contracted'),
        ('sp_approved','Study Plan Approved'),
        ('requested','Requested'),
        ('received','Received'),
        ('approved','Approved'),
        ('rejected','Rejected'),
        ('cancelled','Cancelled'),
    ]
    _track = {
        'state': {
            'sgr.study_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'sgr.study_contracted': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'contracted',
            'sgr.study_sp_approved': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'sp_approved',
            'sgr.study_requested': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'requested',
            'sgr.study_received': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'received',
            'sgr.study_approved': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'approved',
            'sgr.study_rejected': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'rejected',
            'sgr.study_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
        },
    }
    _columns = {
        'sgr_document_id': fields.many2one('sgr.document', 'Documents', ondelete='cascade', required=True, help=u""""""),
        'product_id': fields.many2one('product.product', string='Product', readonly=True, states={'draft': [('readonly', False)]}),
        'source': fields.selection([(u'supplier', u'Supplier'), (u'own', u'Own')], string='Source', readonly=True),
        'laboratory_id': fields.many2one('res.partner', string='Laboratory', readonly=True, states={'draft': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}, context={'default_is_laboratory':'True','default_is_company':'True'}, domain=[('is_laboratory','=',True)]),
        'supplier_id': fields.many2one('res.partner', string='Supplier', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}, context={'default_supplier':'True','default_is_company':'True'}, domain=[('supplier','=',True)]),
        'start_date': fields.date(string='Start Date', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}),
        'end_date': fields.date(string='End Date', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}),
        'concentration': fields.float(string='Concentration', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}),
        'concentration_uom_id': fields.many2one('product.uom', string='Concentration UOM', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}),
        'director_author_id': fields.many2one('res.partner', string='Director/Author', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}),
        'summary': fields.html(string='Summary', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}),
        'result': fields.html(string='Result', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}),
        'validation_method': fields.html(string='Validation Method', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}, translate=True),
        'report_other_study': fields.boolean(string='Report in another study?'),
        'glp': fields.boolean(string='GLP'),
        'summary_es': fields.html(string='Summary Spanish', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}),
        'summary_pt': fields.html(string='Summary Portuguese', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}),
        'result_es': fields.html(string='Result Spanish', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}),
        'result_pt': fields.html(string='Result Portuguese', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}),
        'validation_method_pt': fields.html(string='Validation Method Portuguese', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}),
        'validation_method_es': fields.html(string='Validation Method Spanish', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}),
        'state': fields.selection(_states_, "State"),
        'product_studies': fields.many2one('sgr.product_study', string='product_studies'), 
        'proposal_id': fields.many2one('sgr.proposal', string='Proposal'), 
        'study_purpose_ids': fields.many2many('sgr.study_purpose', 'sgr_study_ids_study_purpose_ids_rel', 'study_id', 'study_purpose_id', string='Study Purpose'), 
        'study_method_ids': fields.many2many('sgr.study_method', 'sgr_study_ids_study_method_ids_rel', 'study_id', 'study_method_id', string='Study Methods'), 
        'experimental_result_ids': fields.one2many('sgr.experimental_result', 'study_id', string='Experimental Results'), 
        'study_presentation_ids': fields.one2many('sgr.study_presentation', 'study_id', string='Presentations', readonly=True), 
        'replace_ids': fields.one2many('sgr.study', 'replaced_by_id', string='Replacing'), 
        'replaced_by_id': fields.many2one('sgr.study', string='Replaced By'), 
        'study_id': fields.many2one('sgr.study', string='Study'), 
        'study_ids': fields.one2many('sgr.study', 'study_id', string='study_ids'), 
        'lang_ids': fields.many2many('res.lang', 'sgr_lang_ids_study_ids_rel', 'study_id', 'lang_id', string='Languages', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)]}), 
    }

    _defaults = {
        'state': 'draft',
        'source': 'supplier',
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
            wf_service.trg_delete(uid, 'sgr.study', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.study', obj_id, cr)
        return True

    def unlink(self, cr, uid, ids, context=None):
        sgr_document_obj = self.pool.get('sgr.document')
        data = self.read(cr, uid, ids, [ 'sgr_document_id', ])
        res = super(study, self).unlink(cr, uid, ids, context=context)
        for item in data:
            sgr_document_obj.unlink(cr, uid, item['sgr_document_id'][0],context=context)
        return res


study()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
