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
    'author': 'Sistemas ADHOC',
    'category': u'base.module_category_knowledge_management',
    'depends': ['sgr'],
    'description': 'Alerts for taxes and sample requests',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': 'SGR Alerts',
    'test': [],
    'demo': [ 
],
    'data': [
#        'res_users_view.xml',
        'data/sgr_alerts_data.xml',
        'cron.xml',
],
    'version': 'No version',
   # 'auto_install': False,
   # 'application': True,
    'website': ''}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
