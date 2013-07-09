# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License AS
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

from openerp.osv import fields,osv
from openerp import tools

class sagi_new_product_project_report(osv.osv):

    _name = "sagi.new_product_project.report"
    _description = "New Product Project Report"
    _auto = False

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

    _snp_status_ = [
        ('rejected','Rejected'),
        ('aborted','Aborted'),
        ('closed','Closed'),
        ('ongoing','Ongoing'),
        ('draft','Draft'),
        ('cancelled','Cancelled'),
    ]

    _columns = {
        'reference': fields.char(string='Reference', readonly=True),
        'name': fields.char(string='Name', readonly=True),
        'agronomic_class': fields.many2one('sgr.agronomic_class', string='Agronomic Class', readonly=True),
#        'next_action_description': fields.char(string='Description', size=256),
#        'next_action_date': fields.date(string='Date'),
#        'next_action_responsible': fields.many2one('res.users', string='Responsible'),
#        'project': fields.many2one('project.project', string='Project'),
        'phase': fields.selection([(u'creation', u'Creation'), (u'initiation', u'Initiation'), (u'planning', u'Planning'), (u'excecution', u'Execution'), (u'closure', u'Closure')], string='Phase', readonly=True),
#        'abort_file': fields.binary(string='Abort'),
#        'privacy_visibility': fields.selection([(u'public', u'Public'), (u'followers', u'Followers Only')], string='Privacy / Visibility', required=True),
        'operative_id': fields.many2one('res.company', readonly=True, string='Operative'),
        'state': fields.selection(_states_, "State", readonly=True),
#        'status_report_ids': fields.one2many('sagi.status_report', 'new_product_project_id', string='Status Reports'), 
#        'npp_gantt_view_ids': fields.one2many('sagi.npp_gantt_view', 'new_product_project_id', string='npp_gantt_view_ids'), 
        'related_product_ids': fields.one2many('sagi.related_product', 'new_product_project_id', readonly=True, string='Related Products'), 
#        'SNP_file': fields.binary(string='SNP', help=u"""Exigido para pasar a etapa &quot;snp presented&quot;"""),
#        'QNP_file': fields.binary(string='QNP'),
#        'CIO_file': fields.binary(string='Operative Innovation Committee'),
#        'summary_file': fields.binary(string='Summary'),
#        'CO_file': fields.binary(string='Operational Committee'),
#        'presentation_file': fields.binary(string='Presentation'),
#        'CIA_file': fields.binary(string='Agrihold Innovation Committee'),
#        'charter_file': fields.binary(string='Project Charter'),
#        'kick_off_ac_file': fields.binary(string='Kick Off Critical Analysis'),
#        'ca_sc_file': fields.binary(string='Supply Chain'),
#        'ca_sc_end_date': fields.date(string='Date to End'),
#        'ca_mtk_file': fields.binary(string='Marketing'),
#        'ca_mtk_end_date': fields.date(string='Date to End'),
#        'ca_dr_file': fields.binary(string='Develp. and Registration'),
#        'ca_dr_end_date': fields.date(string='Date to End'),
#        'ca_result_file': fields.binary(string='Result'),
#        'ca_result_end_date': fields.date(string='Date to End'),
#        'kick_off_project_file': fields.binary(string='Project Kick Off'),

        'budget': fields.float(string='Budjet (USD)', readonly=True),
        'project_leader': fields.many2one('res.users', string='Project Leader', readonly=True),
        'project_sponsor': fields.many2one('res.users', string='Project Sponsor', readonly=True),
        'interested_operative_ids': fields.many2many('res.company', 'sagi___interested_operative_ids_rel', 'new_product_project_id', 'company_id', string='Interested Operatives', readonly=True), 
#        'closing_report_file': fields.binary(string='Closing Report', readonly=True),
        'nbr': fields.integer(string='# of Projects', readonly=True),
        'delay': fields.integer('Project Delay', readonly=True, group_operator="avg"),
        'delay_status': fields.char('Delay Status', readonly=True),
        'creation_date_to_start': fields.date(string='Date to Start', readonly=True),
        'creation_date_to_end': fields.date(string='Date to End', readonly=True),
        'creation_started_date': fields.date(string='Started Date', readonly=True),
        'creation_end_date': fields.date(string='End Date', readonly=True),
        'initiation_date_to_start': fields.date(string='Date to Start', readonly=True),
        'initiation_date_to_end': fields.date(string='Date to End', readonly=True),
        'initiation_started_date': fields.date(string='Started Date', readonly=True),
        'initiation_end_date': fields.date(string='End Date', readonly=True),
        'date_to_end': fields.date(string='Expected End Date', readonly=True),
        'closure_date_to_start': fields.date(string='Date to Start', readonly=True),
        'closure_date_to_end': fields.date(string='Date to End', readonly=True),
        'closure_started_date': fields.date(string='Started Date', readonly=True),
        'closure_end_date': fields.date(string='End Date', readonly=True),
        'planning_date_to_start': fields.date(string='Date to Start', readonly=True),
        'planning_date_to_end': fields.date(string='Date to End', readonly=True),
        'planning_started_date': fields.date(string='Started Date', readonly=True),
        'planning_end_date': fields.date(string='End Date', readonly=True),
        'excecution_date_to_start': fields.date(string='Date to Start', readonly=True),
        'excecution_date_to_end': fields.date(string='Date to End', readonly=True),
        'excecution_started_date': fields.date(string='Started Date', readonly=True),
        'excecution_end_date': fields.date(string='End Date', readonly=True),

        'date_to_end_year': fields.char(string='Year to End', readonly=True),
        'date_to_end_month': fields.char(string='Month to End', readonly=True),

        'creation_started_year': fields.char(string='Started Year', readonly=True),
        'creation_started_month': fields.char(string='Started Month', readonly=True),

        'closure_date_to_end_year': fields.char(string='Year to End', readonly=True),
        'closure_date_to_end_month': fields.char(string='Mont to End', readonly=True),

        'closure_end_year': fields.char(string='Year End', readonly=True),
        'closure_end_month': fields.char(string='Month End', readonly=True),

        'snp_status': fields.selection(string='SNP Status', selection=_snp_status_),
    }

    _order = 'id desc'

    def init(self, cr):

        tools.drop_view_if_exists(cr, 'sagi_new_product_project_report')
        cr.execute("""
            CREATE OR REPLACE VIEW sagi_new_product_project_report AS (
            SELECT  
                    CAST(c.id AS text) AS id,

                    to_char(c.date_to_end, 'YYYY') as date_to_end_year,
                    to_char(c.date_to_end, 'MM-YY') as date_to_end_month,

                    to_char(c.creation_started_date, 'YYYY') as creation_started_year,
                    to_char(c.creation_started_date, 'MM-YY') as creation_started_month,

                    to_char(c.closure_date_to_end, 'YYYY') as closure_date_to_end_year,
                    to_char(c.closure_date_to_end, 'MM-YY') as closure_date_to_end_month,

                    to_char(c.closure_end_date, 'YYYY') as closure_end_year,
                    to_char(c.closure_end_date, 'MM-YY') as closure_end_month,

                    CASE
                     WHEN closure_end_date is null
                        THEN (now()::date - date_to_end)
                        ELSE (closure_end_date - date_to_end)
                    END AS delay,

                    CASE
                     WHEN (now()::date - date_to_end) > 0
                        THEN 'Delayed'
                        ELSE 'Ok'
                    END AS delay_status,

                    snp_status,
                    planning_started_date, 
                    reference, 
                    ca_result_end_date, 
                    excecution_date_to_start, 
                    project_leader, 
                    phase, 
                    closure_date_to_end, 
                    closure_end_date, 
                    excecution_started_date, 
                    ca_dr_end_date, 
                    project, 
                    closure_date_to_start, 
                    initiation_end_date, 
                    agronomic_class, 
                    excecution_date_to_end, 
                    ca_sc_file, 
                    date_to_end, 
                    privacy_visibility, 
                    state, 
                    creation_date_to_start, 
                    creation_started_date, 
                    project_sponsor, 
                    excecution_end_date, 
                    ca_sc_end_date, 
                    creation_end_date, 
                    planning_date_to_start, 
                    closure_started_date, 
                    next_action_responsible, 
                    ca_mtk_end_date, 
                    name, 
                    planning_end_date, 
                    creation_date_to_end, 
                    budget, charter_file, summary_file, 
                    initiation_date_to_start, 
                    initiation_started_date, 
                    initiation_date_to_end, 
                    planning_date_to_end, 
                    user_id,
                    operative_id,
                    1 AS nbr
            FROM sagi_new_product_project c
        )""")

sagi_new_product_project_report()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
