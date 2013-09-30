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


{   'active': False,
    'author': 'No author.',
    'category': u'base.module_category_knowledge_management',
    'demo_xml': [],
    'depends': [u'project', u'mail', u'account', u'sgr', u'product'],
    'description': u'SAGI',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': u'SAGI',
    'test': [],
    'update_xml': [   u'security/sagi_group.xml',
                      u'view/new_product_project_view.xml',
                      u'view/npp_creation_view.xml',
                      u'view/npp_initiation_view.xml',
                      u'view/npp_planning_view.xml',
                      u'view/npp_closure_view.xml',
                      u'view/npp_excecution_view.xml',
                      u'view/related_product_view.xml',
                      u'view/related_product_tag_view.xml',
                      u'view/npp_gantt_view_view.xml',
                      u'view/status_report_view.xml',
                      u'view/config_settings_view.xml',
                      u'view/sagi_menuitem.xml',
                      u'data/new_product_project_properties.xml',
                      u'data/npp_creation_properties.xml',
                      u'data/npp_initiation_properties.xml',
                      u'data/npp_planning_properties.xml',
                      u'data/npp_closure_properties.xml',
                      u'data/npp_excecution_properties.xml',
                      u'data/related_product_properties.xml',
                      u'data/related_product_tag_properties.xml',
                      u'data/npp_gantt_view_properties.xml',
                      u'data/status_report_properties.xml',
                      u'data/config_settings_properties.xml',
                      u'data/new_product_project_track.xml',
                      u'data/npp_creation_track.xml',
                      u'data/npp_initiation_track.xml',
                      u'data/npp_planning_track.xml',
                      u'data/npp_closure_track.xml',
                      u'data/npp_excecution_track.xml',
                      u'data/related_product_track.xml',
                      u'data/related_product_tag_track.xml',
                      u'data/npp_gantt_view_track.xml',
                      u'data/status_report_track.xml',
                      u'data/config_settings_track.xml',
                      u'workflow/npp_creation_workflow.xml',
                      u'workflow/npp_planning_workflow.xml',
                      u'workflow/npp_excecution_workflow.xml',
                      u'workflow/npp_closure_workflow.xml',
                      u'workflow/npp_initiation_workflow.xml',
                      u'workflow/new_product_project_workflow.xml',
                      'security/ir.model.access.csv'],
    'version': 'No version',
    'website': ''}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
