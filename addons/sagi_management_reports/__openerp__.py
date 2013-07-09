# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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


{
    'active': True,
    'name': 'SAGI Management Reports',
    'category': 'SGR', 
    'version': '1.0',
    'description': """
    Reports for SAGI management
    """,
    'author': 'Sistemas Adhoc',
    'website': 'http://www.sistemasadhoc.com.ar/',
    'depends': ['sagi','sgr','project','sgr_reports','competitiveness_management_reports'],
    'data': [
    'security/security.xml',
    'report/new_product_project_crm_report.xml',
    'security/ir.model.access.csv',
    'board_crm_view.xml',
#    'board_crm_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
