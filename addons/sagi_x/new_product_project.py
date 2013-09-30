# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Business Applications
#    Copyright (C) 2004-2012 OpenERP S.A. (<http://openerp.com>).
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

from openerp.osv import fields, osv
from openerp.tools.translate import _

from datetime import datetime, timedelta
import locale
import res_config_parameters

class new_product_project(osv.osv):
    _inherit = 'sagi.new_product_project'

    _snp_status_ = [
        ('rejected','Rejected'),
        ('aborted','Aborted'),
        ('closed','Closed'),
        ('ongoing','Ongoing'),
        ('draft','Draft'),
        ('cancelled','Cancelled'),
    ]

    def _get_snp_status(self, cr, uid, ids, field_name, args, context=None):
        ret = {}
        for npp in self.browse(cr, uid, ids, context=None):
            if npp.state == 'qnp_rejected' or npp.state == 'rejected_by_cio' or npp.state == 'rejected_by_co' or npp.state == 'rejected_by_cia' or npp.state == 'rejected_by_ca':
                ret[npp.id] = 'rejected'
            elif npp.state == 'aborted':
                ret[npp.id] = 'aborted'
            elif npp.state == 'project_closed':
                ret[npp.id] = 'closed'
            elif npp.state == 'draft_snp':
                ret[npp.id] = 'draft'
            elif npp.state == 'cancelled':
                ret[npp.id] = 'cancelled'                
            else:
                ret[npp.id] = 'ongoing'
        return ret

    
    _columns = {
        'user_id': fields.many2one('res.users', string='User'),
        'creation_gantt_id': fields.many2one('sagi.npp_gantt_view', 'Creation'),
        'initiation_gantt_id': fields.many2one('sagi.npp_gantt_view', 'Initiation'),
        'planning_gantt_id': fields.many2one('sagi.npp_gantt_view', 'Planning'),
        'execution_gantt_id': fields.many2one('sagi.npp_gantt_view', 'Execution'),
        'closure_gantt_id': fields.many2one('sagi.npp_gantt_view', 'Closure'),
        
        'planning_pred_term': fields.integer(string='Planning term (days)'),
        'execution_pred_term': fields.integer(string='Execution term (days)'), 
        'closing_pred_term': fields.integer(string='Closing term (days)'), 
        
        'related_project_date_to_start': fields.related('project', 'date_start_by_subproject', type='date',
                        string='Date to Start', readonly=True),
        'related_project_date_to_finish': fields.related('project', 'date_end_by_subproject', type='date',
                        string='Date to End', readonly=True),
        
        'snp_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='SNP Attachment'),
        'snp_file_attachment_file': fields.related('snp_file_attachment', 'datas', type='binary',
                        string='SNP Template', readonly=True),
        
        'qnp_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='QNP Attachment'),
        'qnp_file_attachment_file': fields.related('qnp_file_attachment', 'datas', type='binary',
                        string='QNP Template', readonly=True),
        
        'cio_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='Operative Innovation Committee Attachment'),
        'cio_file_attachment_file': fields.related('cio_file_attachment', 'datas', type='binary',
                        string='Operative Innovation Committee Template', readonly=True),
        
        'summary_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='Summary Attachment'),
        'summary_file_attachment_file': fields.related('summary_file_attachment', 'datas', type='binary',
                        string='Summary Template', readonly=True),
        
        'co_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='Operational Committee Attachment'),
        'co_file_attachment_file': fields.related('co_file_attachment', 'datas', type='binary',
                        string='Operational Committee Template', readonly=True),
        
        'presentation_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='Presentation Attachment'),
        'presentation_file_attachment_file': fields.related('presentation_file_attachment', 'datas', type='binary',
                        string='Presentation Template', readonly=True),
        
        'cia_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='Agrihold Innovation Committee Attachment'),
        'cia_file_attachment_file': fields.related('cia_file_attachment', 'datas', type='binary',
                        string='Agrihold Innovation Committee Template', readonly=True),
        
        'charter_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='Project Charter Attachment'),
        'charter_file_attachment_file': fields.related('charter_file_attachment', 'datas', type='binary',
                        string='Project Charter Template', readonly=True),
        
        'kick_off_ac_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='Kick Off Critical Analysis Attachment'),
        'kick_off_ac_file_attachment_file': fields.related('kick_off_ac_file_attachment', 'datas', type='binary',
                        string='Kick Off Critical Analysis Template', readonly=True),
        
        'ca_sc_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='Supply Chain Attachment'),
        'ca_sc_file_attachment_file': fields.related('ca_sc_file_attachment', 'datas', type='binary',
                        string='Supply Chain Template', readonly=True),
        
        'ca_mkt_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='Marketing Attachment'),
        'ca_mkt_file_attachment_file': fields.related('ca_mkt_file_attachment', 'datas', type='binary',
                        string='Marketing Template', readonly=True),
        
        'ca_dr_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='Develp. and Registration Attachment'),
        'ca_dr_file_attachment_file': fields.related('ca_dr_file_attachment', 'datas', type='binary',
                        string='Develp. and Registration Template', readonly=True),
        
        'ca_result_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='Result Attachment'),
        'ca_result_file_attachment_file': fields.related('ca_result_file_attachment', 'datas', type='binary',
                        string='Result Template', readonly=True),
        
        'kick_off_project_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='Project Kick Off Attachment'),
        'kick_off_project_file_attachment_file': fields.related('kick_off_project_file_attachment', 'datas', type='binary',
                        string='Project Kick Off Template', readonly=True),
        
        'closing_report_file_attachment': fields.property('ir.attachment', type='many2one', relation='ir.attachment',
                        view_load=True, string='Closing Report Attachment'),
        'closing_report_file_attachment_file': fields.related('closing_report_file_attachment', 'datas', type='binary',
                        string='Closing Report Template', readonly=True),
        'snp_status': fields.function(
                    _get_snp_status,
                    string = 'SNP Status', type='selection', selection=_snp_status_,
                    store = {
                        'sagi.new_product_project': (lambda self, cr, uid, ids, c={}: ids, ['state'], 10)
                    }),
    }
    
    def default_planning_pred_term(self, cr, uid, context=None):
        config_settings = self.pool.get('sagi.config_settings')
        ret = config_settings.get_default_planning_pred_term(cr, uid, [], context=context)
        return ret.get('planning_pred_term', 0)
        
    def default_closing_pred_term(self, cr, uid, context=None):
        config_settings = self.pool.get('sagi.config_settings')
        ret = config_settings.get_default_closing_pred_term(cr, uid, [], context=context)
        return ret.get('closing_pred_term', 0)
        
    _defaults = {
        'phase': u'creation',
        'planning_pred_term': default_planning_pred_term,
        'closing_pred_term': default_closing_pred_term,
        'user_id': lambda obj, cr, uid, context: uid,
        'privacy_visibility': 'followers',
    }
    
    
    def create(self, cr, uid, vals, context=None):
        self.control_dates_from_create(cr, uid, vals, context=context)
        
        vals = self.update_vals_with_dates_from_create(cr, uid, vals, context=context)
        new_id = super(new_product_project, self).create(cr, uid, vals, context=context)
        if isinstance(new_id, list):
            new_id = new_id[0]
        
        gantt_view_obj = self.pool.get('sagi.npp_gantt_view')
        
        gantt_vals = {}
        gantt_vals['name'] = 'Creation'
        gantt_vals['sequence'] = 1
        gantt_vals['new_product_project_id'] = new_id
        creation_id = gantt_view_obj.create(cr, uid, gantt_vals, context=context)
        
        gantt_vals = {}
        gantt_vals['name'] = 'Initiation'
        gantt_vals['sequence'] = 2
        gantt_vals['new_product_project_id'] = new_id
        initiation_id = gantt_view_obj.create(cr, uid, gantt_vals, context=context)
        
        gantt_vals = {}
        gantt_vals['name'] = 'Planning'
        gantt_vals['sequence'] = 3
        gantt_vals['new_product_project_id'] = new_id
        planning_id = gantt_view_obj.create(cr, uid, gantt_vals, context=context)
        
        gantt_vals = {}
        gantt_vals['name'] = 'Execution'
        gantt_vals['sequence'] = 4
        gantt_vals['new_product_project_id'] = new_id
        execution_id = gantt_view_obj.create(cr, uid, gantt_vals, context=context)
        
        gantt_vals = {}
        gantt_vals['name'] = 'Closure'
        gantt_vals['sequence'] = 5
        gantt_vals['new_product_project_id'] = new_id
        closure_id = gantt_view_obj.create(cr, uid, gantt_vals, context=context)
        
        new_vals = {}
        new_vals['creation_gantt_id'] = creation_id
        new_vals['initiation_gantt_id'] = initiation_id
        new_vals['planning_gantt_id'] = planning_id
        new_vals['execution_gantt_id'] = execution_id
        new_vals['closure_gantt_id'] = closure_id
        
        self.write(cr, uid, [new_id], new_vals, context=context)
        
        self.update_gantt_views(cr, uid, [new_id], vals, context=context)
        
        return new_id
    
    def write(self, cr, uid, ids, vals, context=None):
#        if 'state' in vals:
#            self.wkf_preconditions(cr, uid, ids, vals, context=context)
# por el momento se eliminan las restricciones de cambio de estado 
        
        self.control_dates_from_write(cr, uid, ids, vals, context=context)
        
        vals = self.update_vals_with_dates_from_write(cr, uid, ids, vals, context=context)
        ret = super(new_product_project, self).write(cr, uid, ids, vals, context=context)
        
        if 'state' in vals:
            self.wkf_posconditions(cr, uid, ids, vals, context=context)
# por el momento se eliminan las restricciones de cambio de estado         
        self.update_gantt_views(cr, uid, ids, vals, context=context)
        
        return ret
    
    
    #
    # Workflow management
    #
    def wkf_preconditions(self, cr, uid, ids, vals, context=None):
        if 'state' not in vals:
            return
        if vals['state'] == 'snp_presented':
            self.check_entering_snp_presented(cr, uid, ids, context=context)
        if vals['state'] in ['approved_by_qnp', 'qnp_rejected']:
            self.check_entering_approved_by_qnp(cr, uid, ids, context=context)
        if vals['state'] in ['approved_by_cio', 'rejected_by_cio']:
            self.check_entering_approved_by_cio(cr, uid, ids, context=context)
        if vals['state'] in ['summary_ready']:
            self.check_entering_summary_ready(cr, uid, ids, context=context)
        if vals['state'] in ['approved_by_co', 'rejected_by_co']:
            self.check_entering_approved_by_co(cr, uid, ids, context=context)
        if vals['state'] in ['presentation_ready']:
            self.check_entering_presentation_ready(cr, uid, ids, context=context)
        if vals['state'] in ['project_charter_draft']:
            self.check_entering_project_charter_draft(cr, uid, ids, context=context)
        if vals['state'] in ['rejected_by_cia']:
            self.check_entering_rejected_by_cia(cr, uid, ids, context=context)
        if vals['state'] in ['preliminary_project_planning']:
            self.check_entering_preliminary_project_planning(cr, uid, ids, context=context)
        if vals['state'] in ['supply_chain_ca_ongoing']:
            self.check_entering_supply_chain_ca_ongoing(cr, uid, ids, context=context)
        if vals['state'] in ['marketing_ca_ongoing']:
            self.check_entering_marketing_ca_ongoing(cr, uid, ids, context=context)
        if vals['state'] in ['dr_ca_ongoing']:
            self.check_entering_dr_ca_ongoing(cr, uid, ids, context=context)
        if vals['state'] in ['ca_evaluation']:
            self.check_entering_ca_evaluation(cr, uid, ids, context=context)
        if vals['state'] in ['project_planning']:
            self.check_entering_project_planning(cr, uid, ids, context=context)
        if vals['state'] in ['project_ongoing']:
            self.check_entering_project_ongoing(cr, uid, ids, context=context)
        if vals['state'] in ['project_review_ongoing']:
            self.check_entering_project_review_ongoing(cr, uid, ids, context=context)
        if vals['state'] in ['project_closure']:
            pass
        if vals['state'] in ['project_closed']:
            self.check_entering_project_closed(cr, uid, ids, context=context)
        if vals['state'] in ['aborted']:
            self.check_entering_aborted(cr, uid, ids, context=context)
        
    def wkf_posconditions(self, cr, uid, ids, vals, context=None):
        if 'state' not in vals:
            return
        if vals['state'] == 'snp_presented':
            self.actions_snp_presented(cr, uid, ids, vals, context=context)
        if vals['state'] in ['project_charter_draft', 'rejected_by_cia']:
            self.actions_project_charter_draft(cr, uid, ids, vals, context=context)
        if vals['state'] in ['preliminary_project_planning']:
            self.actions_preliminary_project_planning(cr, uid, ids, vals, context=context)
        if vals['state'] in ['project_planning']:
            self.actions_project_planning(cr, uid, ids, vals, context=context)
        if vals['state'] in ['project_ongoing']:
            self.actions_project_ongoing(cr, uid, ids, vals, context=context)
        if vals['state'] in ['project_review_ongoing']:
            self.actions_project_review_ongoing(cr, uid, ids, vals, context=context)
        if vals['state'] in ['project_closed']:
            self.actions_project_closed(cr, uid, ids, vals, context=context)
        
    # Entering SNP Presented
    
    def check_entering_snp_presented(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.SNP_file:
                raise osv.except_osv(_('SNP file not found.'),
                            _('Cannot move Product to next stage, an SPN file should be provided first.'))
    
    def actions_snp_presented(self, cr, uid, ids, vals, context=None):
        sequence_obj = self.pool.get('ir.sequence')
        for project in self.browse(cr, uid, ids, context=context):
            new_vals = {}
            if not project.reference:
                reference = sequence_obj.next_by_id(cr, uid, project.agronomic_class.sequence_id.id, context=context)
                new_vals['reference'] = reference
            
            now = datetime.now()
            new_vals['creation_date_to_start'] = now.strftime("%Y-%m-%d")
            
            config_parameters = self.pool.get('ir.config_parameter')
            creation_duration_str = config_parameters.get_param(cr, uid, res_config_parameters.parameter_creation_duration,
                                        context=context)
            if not creation_duration_str:
                creation_duration = 0
            else:
                try:
                    creation_duration = int(creation_duration_str)
                except exception:
                    creation_duration = 0
            
            end_date = now + timedelta(days=creation_duration)
            new_vals['creation_date_to_end'] = end_date.strftime("%Y-%m-%d")
            
            new_vals['creation_started_date'] = now.strftime("%Y-%m-%d")
            
            self.write(cr, uid, project.id, new_vals, context=context)
    
    # Entering Approved by QNP
    
    def check_entering_approved_by_qnp(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.QNP_file:
                raise osv.except_osv(_('QNP file not found.'),
                            _('Cannot move Product to next stage, a QNP file should be provided first.'))
    
    # Entering Approved by CIO
    
    def check_entering_approved_by_cio(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.CIO_file:
                raise osv.except_osv(_('CIO file not found.'),
                            _('Cannot move Product to next stage, a CIO file should be provided first.'))
    
    # Entering Summary Ready
    
    def check_entering_summary_ready(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.summary_file:
                raise osv.except_osv(_('Summary file not found.'),
                            _('Cannot move Product to next stage, a Summary file should be provided first.'))
    
    # Entering Approved by CO
    
    def check_entering_approved_by_co(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.CO_file:
                raise osv.except_osv(_('CO file not found.'),
                            _('Cannot move Product to next stage, a CO file should be provided first.'))
    
    # Entering Presentation Ready
    
    def check_entering_presentation_ready(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.presentation_file:
                raise osv.except_osv(_('Presentation file not found.'),
                            _('Cannot move Product to next stage, a Presentation file should be provided first.'))
    
    # Entering Project Charter Draft
    
    def check_entering_project_charter_draft(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.CIA_file:
                raise osv.except_osv(_('Agrihold Innovation Committee file not found.'),
                            _('Cannot move Product to next stage, a Agrihold Innovation Committee file should be provided first.'))
            if not project.date_to_end:
                raise osv.except_osv(_('Project Expected End Date not specified.'),
                            _('Cannot move Product to next stage, a Project Expected End Date should be provided first.'))
            if not project.project_leader:
                raise osv.except_osv(_('Project Leader not specified.'),
                            _('Cannot move Product to next stage, a Project Leader should be provided first.'))
            if not project.project_sponsor:
                raise osv.except_osv(_('Project Sponsor not specified.'),
                            _('Cannot move Product to next stage, a Project Sponsor should be provided first.'))
    
    def actions_project_charter_draft(self, cr, uid, ids, vals, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            new_vals = {'phase': u'initiation'}
            new_vals['creation_end_date'] = datetime.now().strftime("%Y-%m-%d")
            self.write(cr, uid, project.id, new_vals, context=context)
    
    # Entering Rejected by CIA
    
    def check_entering_rejected_by_cia(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.CIA_file:
                raise osv.except_osv(_('Agrihold Innovation Committee file not found.'),
                            _('Cannot move Product to next stage, a Agrihold Innovation Committee file should be provided first.'))
            
    # Entering Preliminary Project Planning
    
    def check_entering_preliminary_project_planning(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.charter_file:
                raise osv.except_osv(_('Project Charter file not found.'),
                            _('Cannot move Product to next stage, a Project Charter file should be provided first.'))
    
    def actions_preliminary_project_planning(self, cr, uid, ids, vals, context=None):
        config_settings = self.pool.get('sagi.config_settings')
        
        ret = config_settings.get_default_ca_sc_pred_term(cr, uid, [], context=context)
        conf_ca_sc_pred_term = ret.get('ca_sc_pred_term', 0)
        
        date_format = '%Y-%m-%d'
        for project in self.browse(cr, uid, ids, context=context):
            new_vals = {}
            
            ca_sc_end_date = datetime.now() + timedelta(days=conf_ca_sc_pred_term)
            new_vals['ca_sc_end_date'] = ca_sc_end_date.strftime(date_format)
            
            ca_mtk_end_date = ca_sc_end_date + timedelta(days=conf_ca_sc_pred_term)
            new_vals['ca_mtk_end_date'] = ca_mtk_end_date.strftime(date_format)
            
            ca_dr_end_date = ca_mtk_end_date + timedelta(days=conf_ca_sc_pred_term)
            new_vals['ca_dr_end_date'] = ca_dr_end_date.strftime(date_format)
            
            ca_result_end_date = ca_dr_end_date + timedelta(days=conf_ca_sc_pred_term)
            new_vals['ca_result_end_date'] = ca_result_end_date.strftime(date_format)
            
            self.write(cr, uid, project.id, new_vals, context=context)
        
    # Entering Supply Chain CA ongoing
    
    def check_entering_supply_chain_ca_ongoing(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.ca_sc_end_date:
                raise osv.except_osv(_('Supply Chain Date to End not specified.'),
                            _('Cannot move Product to next stage, a Supply Chain Date to End should be specified first.'))
            if not project.ca_mtk_end_date:
                raise osv.except_osv(_('Marketing Date to End not specified.'),
                            _('Cannot move Product to next stage, a Marketing Date to End should be specified first.'))
            if not project.ca_dr_end_date:
                raise osv.except_osv(_('Develp. and Registration Date to End not specified.'),
                            _('Cannot move Product to next stage, a Develp. and Registration Date to End should be specified first.'))
            if not project.ca_result_end_date:
                raise osv.except_osv(_('Result Date to End not specified.'),
                            _('Cannot move Product to next stage, a Result Date to End should be specified first.'))
            if not project.project:
                raise osv.except_osv(_('Project not specified.'),
                            _('Cannot move Product to next stage, a Project should be specified first.'))
            if not project.kick_off_ac_file:
                raise osv.except_osv(_('Kick Off Critical Analysis file not found.'),
                            _('Cannot move Product to next stage, a Kick Off Critical Analysis file should be provided first.'))
    
    # Entering Marketing CA ongoing
    
    def check_entering_marketing_ca_ongoing(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.ca_sc_file:
                raise osv.except_osv(_('Supply Chain file not found.'),
                            _('Cannot move Product to next stage, a Supply Chain file should be provided first.'))
    
    # Entering DR CA ongoing
    
    def check_entering_dr_ca_ongoing(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.ca_mtk_file:
                raise osv.except_osv(_('Marketing file not found.'),
                            _('Cannot move Product to next stage, a Marketing file should be provided first.'))
    
    # Entering CA Evaluation
    
    def check_entering_ca_evaluation(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.ca_dr_file:
                raise osv.except_osv(_('Develp. and Registration file not found.'),
                            _('Cannot move Product to next stage, a Develp. and Registration file should be provided first.'))
    
    # Entering Project Planning
    
    def check_entering_project_planning(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.ca_result_file:
                raise osv.except_osv(_('Result file not found.'),
                            _('Cannot move Product to next stage, a Result file should be provided first.'))
    
    def actions_project_planning(self, cr, uid, ids, vals, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            new_vals = {'phase': u'planning'}
            new_vals['initiation_end_date'] = datetime.now().strftime("%Y-%m-%d")
            self.write(cr, uid, project.id, new_vals, context=context)
    
    # Entering Project Ongoing
    
    def check_entering_project_ongoing(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.kick_off_project_file:
                raise osv.except_osv(_('Project Kick Off file not found.'),
                            _('Cannot move Product to next stage, a Project Kick Off file should be provided first.'))
            if not project.project:
                raise osv.except_osv(_('Project not specified.'),
                            _('Cannot move Product to next stage, a Project should be specified first.'))
            if project.project.state not in ['open']:
                raise osv.except_osv(_('Project not In Progress.'),
                            _('Cannot move Product to next stage, the associated Project should be In Progress.'))
    
    def actions_project_ongoing(self, cr, uid, ids, vals, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            new_vals = {'phase': u'excecution'}
            new_vals['planning_end_date'] = datetime.now().strftime("%Y-%m-%d")
            self.write(cr, uid, project.id, new_vals, context=context)
    
    # Entering Project Ongoing
    
    def check_entering_project_review_ongoing(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.project:
                raise osv.except_osv(_('Project not specified.'),
                            _('Cannot move Product to next stage, a Project should be specified first.'))
            if project.project.state not in ['close']:
                raise osv.except_osv(_('Project not closed.'),
                            _('Cannot move Product to next stage, the associated Project must be closed first.'))
        
    def actions_project_review_ongoing(self, cr, uid, ids, vals, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            new_vals = {'phase': u'closure'}
            new_vals['excecution_end_date'] = datetime.now().strftime("%Y-%m-%d")
            self.write(cr, uid, project.id, new_vals, context=context)
    
    # Entering Project Closed
    
    def check_entering_project_closed(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.closing_report_file:
                raise osv.except_osv(_('Closing Report file not found.'),
                            _('Cannot move Product to next stage, a Closing Report file should be provided first.'))
        
    def actions_project_closed(self, cr, uid, ids, vals, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            new_vals = {}
            new_vals['closure_end_date'] = datetime.now().strftime("%Y-%m-%d")
            self.write(cr, uid, project.id, new_vals, context=context)
    
    # Entering Aborted
    
    def check_entering_aborted(self, cr, uid, ids, context=None):
        for project in self.browse(cr, uid, ids, context=context):
            if not project.abort_file:
                raise osv.except_osv(_('Abort file not found.'),
                            _('Cannot move Product to next stage, an Abort file should be provided first.'))
    
    #
    # Update dates
    #
    def update_vals_with_dates_from_create(self, cr, uid, vals, context=None):
        return self.update_vals_with_dates(cr, uid, vals, False, context=context)
    
    def update_vals_with_dates_from_write(self, cr, uid, ids, vals, context=None):
        npp = self.browse(cr, uid, ids, context=context)
        if isinstance(npp, list):
            npp = npp[0]
        return self.update_vals_with_dates(cr, uid, vals, npp, context=context)
    
    def update_vals_with_dates(self, cr, uid, vals, npp, context=None):
        if 'creation_end_date' in vals:
            vals['initiation_started_date'] = vals['creation_end_date']
        
        if 'initiation_end_date' in vals:
            vals['planning_started_date'] = vals['initiation_end_date']
        
        if 'planning_end_date' in vals:
            vals['excecution_started_date'] = vals['planning_end_date']
        
        if 'excecution_end_date' in vals:
            vals['closure_started_date'] = vals['excecution_end_date']
        
        
        if 'creation_date_to_end' in vals:
            vals['initiation_date_to_start'] = vals['creation_date_to_end']
        
        
        if 'ca_result_end_date' in vals:
            vals['initiation_date_to_end'] = vals['ca_result_end_date']
            vals['planning_date_to_start'] = vals['ca_result_end_date']
        
        date_format = '%Y-%m-%d'
        
        if 'planning_date_to_start' in vals or 'planning_pred_term' in vals:
            planning_date_to_start = vals.get('planning_date_to_start', False)
            if planning_date_to_start:
                planning_date_to_start = datetime.strptime(planning_date_to_start, date_format)
            else:
                if npp:
                    planning_date_to_start = npp.planning_date_to_start
            
            if planning_date_to_start and isinstance(planning_date_to_start, str):
                planning_date_to_start = datetime.strptime(planning_date_to_start, date_format)
            
            if planning_date_to_start:
                planning_pred_term = vals.get('planning_pred_term', False)
                if planning_pred_term:
                    planning_pred_term = int(planning_pred_term)
                elif npp:
                    planning_pred_term = npp.planning_pred_term
                
                if not planning_pred_term:
                    planning_pred_term = 0
                
                planning_date_to_end = planning_date_to_start + timedelta(days=planning_pred_term)
                
                vals['planning_date_to_end'] = planning_date_to_end.strftime(date_format)
                vals['excecution_date_to_start'] = vals['planning_date_to_end']
        
        
        if 'excecution_date_to_start' in vals or 'execution_pred_term' in vals:
            excecution_date_to_start = vals.get('excecution_date_to_start', False)
            if excecution_date_to_start:
                excecution_date_to_start = datetime.strptime(excecution_date_to_start, date_format)
            else:
                if npp:
                    excecution_date_to_start = npp.excecution_date_to_start
            
            if excecution_date_to_start and isinstance(excecution_date_to_start, str):
                excecution_date_to_start = datetime.strptime(excecution_date_to_start, date_format)
                
            if excecution_date_to_start:
                execution_pred_term = vals.get('execution_pred_term', False)
                if execution_pred_term:
                    execution_pred_term = int(execution_pred_term)
                elif npp:
                    execution_pred_term = npp.execution_pred_term
                
                if not execution_pred_term:
                    execution_pred_term = 0
                
                excecution_date_to_end = excecution_date_to_start + timedelta(days=execution_pred_term)
                
                vals['excecution_date_to_end'] = excecution_date_to_end.strftime(date_format)
                vals['closure_date_to_start'] = vals['excecution_date_to_end']
        
        
        if 'closure_date_to_start' in vals or 'closing_pred_term' in vals:
            closure_date_to_start = vals.get('closure_date_to_start', False)
            if closure_date_to_start:
                closure_date_to_start = datetime.strptime(closure_date_to_start, date_format)
            else:
                if npp:
                    closure_date_to_start = npp.closure_date_to_start
            
            if closure_date_to_start and isinstance(closure_date_to_start, str):
                closure_date_to_start = datetime.strptime(closure_date_to_start, date_format)
                
            if closure_date_to_start:
                closing_pred_term = vals.get('closing_pred_term', False)
                if closing_pred_term:
                    closing_pred_term = int(closing_pred_term)
                elif npp:
                    closing_pred_term = npp.closing_pred_term
                
                if not closing_pred_term:
                    closing_pred_term = 0
                
                closure_date_to_end = closure_date_to_start + timedelta(days=closing_pred_term)
                
                vals['closure_date_to_end'] = closure_date_to_end.strftime(date_format)
        
        return vals
    
    #
    # Update Gantt Views
    #
    def update_gantt_views(self, cr, uid, ids, vals, context=None):
        if not isinstance(ids, list):
            ids = [ids]
        gantt_view_obj = self.pool.get('sagi.npp_gantt_view')
        
        for npp in self.browse(cr, uid, ids, context=context):
            if 'creation_date_to_start' in vals:
                gantt_view_obj.write(cr, uid, [npp.creation_gantt_id.id], {'date_start': vals['creation_date_to_start']},
                                     context=context)
            if 'creation_date_to_end' in vals:
                gantt_view_obj.write(cr, uid, [npp.creation_gantt_id.id], {'date_stop': vals['creation_date_to_end']},
                                     context=context)
            
            if 'initiation_date_to_start' in vals:
                gantt_view_obj.write(cr, uid, [npp.initiation_gantt_id.id], {'date_start': vals['initiation_date_to_start']},
                                     context=context)
            if 'initiation_date_to_end' in vals:
                gantt_view_obj.write(cr, uid, [npp.initiation_gantt_id.id], {'date_stop': vals['initiation_date_to_end']},
                                     context=context)
            
            if 'planning_date_to_start' in vals:
                gantt_view_obj.write(cr, uid, [npp.planning_gantt_id.id], {'date_start': vals['planning_date_to_start']},
                                     context=context)
            if 'planning_date_to_end' in vals:
                gantt_view_obj.write(cr, uid, [npp.planning_gantt_id.id], {'date_stop': vals['planning_date_to_end']},
                                     context=context)
            
            if 'execution_date_to_start' in vals:
                gantt_view_obj.write(cr, uid, [npp.execution_gantt_id.id], {'date_start': vals['execution_date_to_start']},
                                     context=context)
            if 'execution_date_to_end' in vals:
                gantt_view_obj.write(cr, uid, [npp.execution_gantt_id.id], {'date_stop': vals['execution_date_to_end']},
                                     context=context)
            
            if 'closure_date_to_start' in vals:
                gantt_view_obj.write(cr, uid, [npp.closure_gantt_id.id], {'date_start': vals['closure_date_to_start']},
                                     context=context)
            if 'closure_date_to_end' in vals:
                gantt_view_obj.write(cr, uid, [npp.closure_gantt_id.id], {'date_stop': vals['closure_date_to_end']},
                                     context=context)
                                     
    #
    # Control of dates
    #
    def control_dates_from_create(self, cr, uid, vals, context=None):
        self.control_dates(cr, uid, False, vals, context=context)
    
    def control_dates_from_write(self, cr, uid, ids, vals, context=None):
        if not isinstance(ids, list):
            ids = [ids]
        for npp in self.browse(cr, uid, ids, context=context):
            self.control_dates(cr, uid, npp, vals, context=context)
    
    def control_dates(self, cr, uid, npp, vals, context=None):
        ca_mtk_end_date = vals.get('ca_mtk_end_date', False)
        if npp and not ca_mtk_end_date:
            ca_mtk_end_date = npp.ca_mtk_end_date
        
        ca_sc_end_date = vals.get('ca_sc_end_date', False)
        if npp and not ca_sc_end_date:
            ca_sc_end_date = npp.ca_sc_end_date
        
        if ca_mtk_end_date and ca_sc_end_date:
            if ca_mtk_end_date < ca_sc_end_date:
                raise osv.except_osv(_('Inconsistency in Dates to End.'),
                        _('Marketing Date to End cannot before Supply Chain Date to End.'))
        
        
        ca_dr_end_date = vals.get('ca_dr_end_date', False)
        if npp and not ca_dr_end_date:
            ca_dr_end_date = npp.ca_dr_end_date
        
        ca_mtk_end_date = vals.get('ca_mtk_end_date', False)
        if npp and not ca_mtk_end_date:
            ca_mtk_end_date = npp.ca_mtk_end_date
        
        if ca_dr_end_date and ca_mtk_end_date:
            if ca_dr_end_date < ca_mtk_end_date:
                raise osv.except_osv(_('Inconsistency in Dates to End.'),
                        _('Develp. and Registration Date to End cannot before Marketing Date to End.'))
        
        
        ca_result_end_date = vals.get('ca_result_end_date', False)
        if npp and not ca_result_end_date:
            ca_result_end_date = npp.ca_result_end_date
        
        ca_dr_end_date = vals.get('ca_dr_end_date', False)
        if npp and not ca_dr_end_date:
            ca_dr_end_date = npp.ca_dr_end_date
        
        if ca_result_end_date and ca_dr_end_date:
            if ca_result_end_date < ca_dr_end_date:
                raise osv.except_osv(_('Inconsistency in Dates to End.'),
                        _('Result Date to End cannot before Develp. and Registration Date to End.'))
new_product_project()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
