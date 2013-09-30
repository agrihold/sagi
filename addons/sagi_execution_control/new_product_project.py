# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011 Eficent (<http://www.eficent.com/>)
#              Jordi Ballester Alomar <jordi.ballester@eficent.com>
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

import tools
from osv import fields, osv
from tools.translate import _

import datetime

class new_product_project(osv.osv):
    _inherit = 'sagi.new_product_project'
    
    _columns = {
        'project_planning': fields.selection((
                        ('red', 'Critical: The "Date to End" of the related Project and/or the execution "Date to End", are greater than "Projected Expected End Date"'),
                        ('yellow', 'Warning: "Date to End" of the related Project is greter than the execution "Date to End"'),
                        ('green', 'On Date')), 'Project Planning',),
        'project_overall_status': fields.selection((
                        ('red', 'Critical: Execution Project related to this New Product Project is in Critical State'),
                        ('yellow', 'Warning: Execution Project related to this New Product Project is in Warning State'),
                        ('green', 'Ok')), 'Project Overall Status',),
        'execution_status': fields.selection((
                        ('red', 'Critical delay: This New Product Project is not in the phase planned for actual date'),
                        ('yellow', 'Delay: This New Product Project is not in the status/stage planned for actual date'),
                        ('green', 'On Time')), 'Execution Status',help="Phases: Initiation, Creation, Planning, Execution, Closure. \nStatus/stages: Draft SNP, SNP Presented, Approved by QNP, etc."),                        
        'overall_status': fields.selection((
                        ('red', 'Critical: at least one alarm of this New Product Project is in Critical state'),
                        ('yellow', 'Warning: at least one alarm of this New Product Project is in Warning state'),
                        ('green', 'Ok')), 'Overall Status', track_visibility='onchange',),
    }

    _track = {
        'overall_status': {
            'sagi_security_control.mt_npp_overall_status_change': lambda self, cr, uid, obj, ctx=None: obj['state'] not in ['new', 'done', 'pending'],
            #ctx=None: obj['overall_status'] in ['warning'],
            #'project_security_control.mt_task_critical': lambda self, cr, uid, obj, ctx=None: obj['overall_status'] in ['critical'],
        },
    },
        
    def compute_control_status(self, cr, uid, ids, context=None):
        datetime_format = '%Y-%m-%d %H:%M:%S'
        date_format = '%Y-%m-%d'
        today = datetime.date.today()
        
        if not isinstance(ids, list):
            ids = [ids]
            
        for npp in self.browse(cr, uid, ids, context=context):
            vals = {}
            
            vals['project_planning'] = 'green'
            if npp.related_project_date_to_finish and npp.excecution_date_to_end:
                related_project_date_to_finish = datetime.datetime.strptime(npp.related_project_date_to_finish,
                                                                            datetime_format).date()
                excecution_date_to_end = datetime.datetime.strptime(npp.excecution_date_to_end, date_format).date()
                if related_project_date_to_finish > excecution_date_to_end:
                    vals['project_planning'] = 'yellow'
            if npp.excecution_date_to_end and npp.date_to_end:
                excecution_date_to_end = datetime.datetime.strptime(npp.excecution_date_to_end, date_format).date()
                date_to_end = datetime.datetime.strptime(npp.date_to_end, date_format).date()
                if excecution_date_to_end > date_to_end:
                    vals['project_planning'] = 'red'
            if npp.related_project_date_to_finish and npp.date_to_end:
                related_project_date_to_finish = datetime.datetime.strptime(npp.related_project_date_to_finish,
                                                                            datetime_format).date()
                date_to_end = datetime.datetime.strptime(npp.date_to_end, datetime_format).date()
                if related_project_date_to_finish > date_to_end:
                    vals['project_planning'] = 'red'
            
            
            vals['project_overall_status'] = 'green'
            if npp.project:
                if npp.project.overall_status == 'yellow':
                    vals['project_overall_status'] = 'yellow'
                elif npp.project.overall_status == 'red':
                    vals['project_overall_status'] = 'red'
            
            
            vals['execution_status'] = 'green'
            if npp.state:
                if npp.state in ['draft_snp', 'snp_presented', 'approved_by_qnp', 'approved_by_cio', 'summary_ready', 'approved_by_co', 'presentation_ready', 'project_charter_draft', 'preliminary_project_planning', 'supply_chain_ca_ongoing']:
                    if npp.ca_sc_end_date:
                        ca_sc_end_date = datetime.datetime.strptime(npp.ca_sc_end_date, date_format).date()
                        if today > ca_sc_end_date:
                            vals['execution_status'] = 'yellow'
                elif npp.state in ['marketing_ca_ongoing']:
                    if npp.ca_mtk_end_date:
                        ca_mtk_end_date = datetime.datetime.strptime(npp.ca_mtk_end_date, date_format).date()
                        if today > ca_mtk_end_date:
                            vals['execution_status'] = 'yellow'
                elif npp.state in ['dr_ca_ongoing']:
                    if npp.ca_dr_end_date:
                        ca_dr_end_date = datetime.datetime.strptime(npp.ca_dr_end_date, date_format).date()
                        if today > ca_dr_end_date:
                            vals['execution_status'] = 'yellow'
                elif npp.state in ['ca_evaluation']:
                    if npp.ca_result_end_date:
                        ca_result_end_date = datetime.datetime.strptime(npp.ca_result_end_date, date_format).date()
                        if today > ca_result_end_date:
                            vals['execution_status'] = 'yellow'
            if npp.phase:
                if npp.phase == 'creation' and npp.creation_date_to_end:
                    creation_date_to_end = datetime.datetime.strptime(npp.creation_date_to_end, date_format).date()
                    if today > creation_date_to_end:
                        vals['execution_status'] = 'red'
                elif npp.phase == 'initiation' and npp.initiation_date_to_end:
                    initiation_date_to_end = datetime.datetime.strptime(npp.initiation_date_to_end, date_format).date()
                    if today > initiation_date_to_end:
                        vals['execution_status'] = 'red'
                elif npp.phase == 'planning' and npp.planning_date_to_end:
                    planning_date_to_end = datetime.datetime.strptime(npp.planning_date_to_end, date_format).date()
                    if today > planning_date_to_end:
                        vals['execution_status'] = 'red'
                elif npp.phase == 'excecution' and npp.excecution_date_to_end:
                    excecution_date_to_end = datetime.datetime.strptime(npp.excecution_date_to_end, date_format).date()
                    if today > excecution_date_to_end:
                        vals['execution_status'] = 'red'
                elif npp.project and npp.project.state and npp.project.state in ['cancelled', 'close'] and npp.initiation_date_to_end:
                    initiation_date_to_end = datetime.datetime.strptime(npp.initiation_date_to_end, date_format).date()
                    if today > initiation_date_to_end:
                        vals['execution_status'] = 'red'
                
            self.write(cr, uid, [npp.id], vals, context=context)
        
        for npp in self.browse(cr, uid, ids, context=context):
            overall_status = 'green'
            
            if npp.project_planning == 'yellow' or npp.project_overall_status == 'yellow' or npp.execution_status == 'yellow':
                overall_status = 'yellow'
            
            if npp.project_planning == 'red' or npp.project_overall_status == 'red' or npp.execution_status == 'red':
                overall_status = 'red'
            
            self.write(cr, uid, [npp.id], {'overall_status': overall_status}, context=context)
        
new_product_project()



