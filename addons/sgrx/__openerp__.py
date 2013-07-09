# -*- coding: utf-8 -*-
##############################################################################
#
#    
#    Copyright (C) 2013 Agrihold - Adhoc - Moldeo.
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
    'author': 'Agrihold - Adhoc - Moldeo',
    'category': 'base.module_category_hidden',
    'demo_xml': [
        u'data/company.xml',
        u'data/document_category.xml',
        u'data/information_category.xml',
        u'data/registry_category.xml',
    ],
    'depends': ['sgr', 'product_expiry','account_accountant','sale','note','auth_oauth','auth_oauth_signup','base_import','document_page','web_shortcuts'],
    'description': 'Extension and adaption of SGR',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': 'Extension and adaption of SGR',
    'test': [
        'test/registry.yml',
        'test/formulated_product.yml',
        'test/contract.yml',
        'test/proposal.yml',
        'test/product_in_ret.yml',
        'test/information.yml',
    ],
    'update_xml': [   
        u'data/analytics.xml',
        u'data/property.xml',
        u'data/sequences.xml',
        u'view/partner_view.xml',
        #u'view/registry_view.xml',
        'view/contract_view.xml',
        'view/proposal_view.xml',
        'view/proposal_product_view.xml',
        'view/product_study_view.xml',        
        'view/ingredient_view.xml',
        'view/formulated_product_registry_view.xml',
        'view/use_recommendation_view.xml',
        'view/information_presentation_view.xml',
        'view/information_view.xml',
        'view/communication_view.xml',
        'view/publication_view.xml',
        'view/technical_product_registry_view.xml',
        'view/component_registry_detail_view.xml',
        'view/component_registry_view.xml',  
        'view/state_registry_view.xml',
        'view/ret_registry_view.xml',
        'view/laboratory_registry_view.xml',
        'view/study_view.xml',
        'view/product_in_ret_view.xml',
        'view/document_move_view.xml',    
        'view/partner_document_view.xml',
        'view/tax_view.xml',
        'view/dossier_document_view.xml',
#        'view/package_file_view.xml',
        'view/official_letter_view.xml',
        'view/packaging_view.xml',
        'view/registry_process_view.xml',
        'view/product_view.xml',
        'view/document_category_view.xml',
        'view/registry_category_view.xml',
        'view/information_category_view.xml',
        'view/partner_role_in_registry_view.xml',
        'view/trademark_registry_view.xml',
        'security/sgrx_security.xml',
        'security/ir.model.access.csv',
        'view/study_presentation_view.xml',
        'view/partner_document_presentation_view.xml',
        'view/sample_request_view.xml',
        'view/stock.xml',
        'view/experimental_result_view.xml',
        'stock_data.xml',
        'sample_request_sequence.xml',
        'workflow/communication_workflow.xml',
        'workflow/contract_workflow.xml',        
        'workflow/document_move_workflow.xml',
        'workflow/information_workflow.xml',
        'workflow/proposal_workflow.xml',
        'workflow/registry_process_workflow.xml',
        'workflow/tax_workflow.xml',
        'workflow/study_workflow.xml',
        'workflow/dossier_document_workflow.xml',
        'workflow/component_registry_workflow.xml',
        'workflow/formulated_product_registry_workflow.xml',
        'workflow/laboratory_registry_workflow.xml',
        'workflow/partner_document_workflow.xml',
        'workflow/ret_registry_workflow.xml',
        'workflow/state_registry_workflow.xml',
        'workflow/technical_product_registry_workflow.xml',
        'view/sgrx_menuitem.xml',
        'view/packaging_capacity_view.xml',
        ],
    'version': '7.0.1.1',
    'website': ''}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
