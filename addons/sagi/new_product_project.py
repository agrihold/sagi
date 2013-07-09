# -*- coding: utf-8 -*-
##############################################################################
#
#    SAGI
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


import re
from openerp import netsvc
from openerp.osv import osv, fields

class new_product_project(osv.osv):
    """"""
    
    _name = 'sagi.new_product_project'
    _description = 'new_product_project'
    _inherits = {  }
    _inherit = [ 'mail.thread' ]

    _states_ = [
        # State machine: npp_workflow
        ('draft_snp','Draft SNP'),
        ('snp_presented','SNP Presented'),
        ('approved_by_qnp','Approved by QNP'),
        ('approved_by_cio','Approved by CIO'),
        ('summary_ready','Summary Ready'),
        ('approved_by_co','Approved by CO'),
        ('presentation_ready','Presentation Ready'),
        ('project_charter_draft','Project Charter Draft'),
        ('preliminary_project_planning','Preliminary Project Planning'),
        ('supply_chain_ca_ongoing','Supply Chain CA ongoing'),
        ('marketing_ca_ongoing','Marketing CA ongoing'),
        ('dr_ca_ongoing','DR CA ongoing'),
        ('ca_evaluation','CA Evaluation'),
        ('project_planning','Project Planning'),
        ('project_ongoing','Project Ongoing'),
        ('project_review_ongoing','Project Review Ongoing'),
        ('project_closure','Project Closure'),
        ('project_closed','Project Closed'),
        ('revise','Revise'),
        ('qnp_rejected','QNP Rejected'),
        ('cancelled','Cancelled'),
        ('rejected_by_cio','Rejected by CIO'),
        ('rejected_by_co','Rejected by CO'),
        ('rejected_by_cia','Rejected by CIA'),
        ('rejected_by_ca','Rejected by CA'),
        ('aborted','Aborted'),
    ]
    _track = {
        'state': {
            'sagi.new_product_project_draft_snp': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft_snp',
            'sagi.new_product_project_snp_presented': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'snp_presented',
            'sagi.new_product_project_approved_by_qnp': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'approved_by_qnp',
            'sagi.new_product_project_approved_by_cio': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'approved_by_cio',
            'sagi.new_product_project_summary_ready': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'summary_ready',
            'sagi.new_product_project_approved_by_co': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'approved_by_co',
            'sagi.new_product_project_presentation_ready': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'presentation_ready',
            'sagi.new_product_project_project_charter_draft': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'project_charter_draft',
            'sagi.new_product_project_preliminary_project_planning': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'preliminary_project_planning',
            'sagi.new_product_project_supply_chain_ca_ongoing': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'supply_chain_ca_ongoing',
            'sagi.new_product_project_marketing_ca_ongoing': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'marketing_ca_ongoing',
            'sagi.new_product_project_dr_ca_ongoing': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'dr_ca_ongoing',
            'sagi.new_product_project_ca_evaluation': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'ca_evaluation',
            'sagi.new_product_project_project_planning': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'project_planning',
            'sagi.new_product_project_project_ongoing': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'project_ongoing',
            'sagi.new_product_project_project_review_ongoing': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'project_review_ongoing',
            'sagi.new_product_project_project_closure': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'project_closure',
            'sagi.new_product_project_project_closed': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'project_closed',
            'sagi.new_product_project_revise': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'revise',
            'sagi.new_product_project_qnp_rejected': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'qnp_rejected',
            'sagi.new_product_project_cancelled': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancelled',
            'sagi.new_product_project_rejected_by_cio': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'rejected_by_cio',
            'sagi.new_product_project_rejected_by_co': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'rejected_by_co',
            'sagi.new_product_project_rejected_by_cia': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'rejected_by_cia',
            'sagi.new_product_project_rejected_by_ca': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'rejected_by_ca',
            'sagi.new_product_project_aborted': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'aborted',
        },
    }
    _columns = {
        'reference': fields.char(string='Reference', help=u"""Completar automáticamente cuando se pasa a estado &quot;on creation&quot;. Se crea con la siguiente sequencia &quot;yyaa000&quot; donde yy son los dos dígitos del año, aa son dos dígitos que representan la clase agronomica (deberíamos heredar clase agroniomica en este modulo y poner un campo &quot;code&quot;) y 000 es la secuencia dentro de esa clase agronomica y dentor lde año. Tal vez también agregar a clase agronomica un m2o a una secuencia.""", readonly=True, size=16),
        'name': fields.char(string='Name', required=True, size=128),
        'agronomic_class': fields.many2one('sgr.agronomic_class', string='Agronomic Class', required=True),
        'next_action_description': fields.char(string='Description', size=256),
        'next_action_date': fields.date(string='Date'),
        'next_action_responsible': fields.many2one('res.users', string='Responsible'),
        'project': fields.many2one('project.project', string='Project'),
        'phase': fields.selection([(u'creation', u'Creation'), (u'initiation', u'Initiation'), (u'planning', u'Planning'), (u'excecution', u'Execution'), (u'closure', u'Closure')], string='Phase', help=u"""Lo debemos poner automaticamente y debe ser readonly en la vista""", readonly=True),
        'abort_file': fields.binary(string='Abort'),
        'privacy_visibility': fields.selection([(u'public', u'Public'), (u'followers', u'Followers Only')], string='Privacy / Visibility', required=True),
        'operative_id': fields.many2one('res.company', string='Operative'),
        'state': fields.selection(_states_, "State"),
        'status_report_ids': fields.one2many('sagi.status_report', 'new_product_project_id', string='Status Reports'), 
        'npp_gantt_view_ids': fields.one2many('sagi.npp_gantt_view', 'new_product_project_id', string='npp_gantt_view_ids'), 
        'related_product_ids': fields.one2many('sagi.related_product', 'new_product_project_id', string='Related Products'), 
    }

    _defaults = {
        'state': 'draft_snp',
        'privacy_visibility': 'public',
        'operative_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.registry', context=c),
    }


    _constraints = [
    ]


    def action_wfk_set_draft_snp(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft_snp'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sagi.new_product_project', obj_id, cr)
            wf_service.trg_create(uid, 'sagi.new_product_project', obj_id, cr)
        return True



new_product_project()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
