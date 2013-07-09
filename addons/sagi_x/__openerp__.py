# -*- coding: utf-8 -*-
##############################################################################
#
#    
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
    'category': 'base.module_category_hidden',
    'depends': ['sagi', 'document', 'project_time_schedule', 'project_state_integration'],
    'description': 'Customizations for SAGI module',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': 'Customizations for SAGI module',
    'test': [],
    'demo': [ 
],
    'data': [   'security/ejemplo_group.xml',
                'data/project_class_data.xml',
                'security/sagi_group.xml',
                'res_config_view.xml',
                'view/agronomic_class_view.xml',
                'view/new_product_project_view.xml',
                'view/ejemplo_menuitem.xml',    
                'wizard/create_default_project_view.xml',
                'view/npp_gantt_view_view.xml',
                'workflow/new_product_project_workflow.xml',
],
    'version': 'No version',
   # 'auto_install': False,
   # 'application': True,
    'website': ''}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
