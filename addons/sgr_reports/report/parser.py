##############################################################################
#
# Copyright (c) 2008-2011 Alistek Ltd (http://www.alistek.com) All Rights Reserved.
#                    General contacts <info@alistek.com>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This module is GPLv3 or newer and incompatible
# with OpenERP SA "AGPL + Private Use License"!
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from report import report_sxw
from report.report_sxw import rml_parse
from datetime import date
from openerp.report import report_sxw
from openerp.tools import float_compare
from openerp import netsvc

class Parser(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(Parser, self).__init__(cr, uid, name, context)
#        self.lang = context.get('lang', 'es_ES')
        if not context:
            context = {}
        self.formulated_product = False
        if context.get('formulated_product_id', False):
            self.formulated_product_id = context['formulated_product_id']
            self.formulated_product = self.pool.get('product.product').browse(self.cr, self.uid, self.formulated_product_id, context=context)

        self.technical_product = False
        if context.get('technical_product_id', False):
            self.technical_product_id = context['technical_product_id']
            self.technical_product = self.pool.get('product.product').browse(self.cr, self.uid, self.technical_product_id, context=context)


        self.localcontext.update({
            'formulated_product': self.formulated_product,
            'technical_product': self.technical_product,
            'custom': self.custom,
            'cqqs': self.cqqs,
            'cqq': self.cqq,
            'ing_other_names': self.ing_other_names,
            'taxes': self.taxes,
            'tax': self.tax,
            'studies': self.studies,
            'study': self.study,
            'p_docs': self.p_docs,
            'p_doc': self.p_doc,
            'informations': self.informations,
            'information': self.information,
            'processes': self.processes,
            'process': self.process,
            'partners': self.partners,
            'partner': self.partner,
            'filter_doc_presentations': self.filter_doc_presentations,
            'get_one_doc_presentation': self.get_one_doc_presentation,
            'filter_inf_presentations': self.filter_inf_presentations,
            'get_one_inf_presentation': self.get_one_inf_presentation,     
            'filter_registries': self.filter_registries,
            'get_one_registry': self.get_one_registry,                        
            'filter_processes': self.filter_processes,
            'get_one_process': self.get_one_process,
            'format_partner_address': self.format_partner_address,
            'today': self.today,
            'today_formated': self.today_formated,
            'as_list': self.as_list,
            'commercial_name': self.commercial_name,
            'myset':self.myset,
            'myget':self.myget,
            'storage':{}
        })

# este no se termino de implementar, la idea es que concatene el separdor. 
    def as_list(self, attr, field,separator=', '):
        expr = "for o in objects:\n\tvalue_list.append(o.%s)" % field
        localspace = {'objects':attr, 'value_list':[]}
        exec expr in localspace
        return localspace['value_list']

    def custom(self, field, kind=0, date=False):
#        field = obj.field
#        if not field:
#            return '[pending2]'
#        if not isinstance(information_presentation_ids, list):
#            information_presentation_ids = [information_presentation_ids]
        ret = ''
        if not field:
            if kind==0:
                ret='[pending]'
            elif kind==1:
                ret='Not applicable'
            elif kind==2:
                ret=''
        else:
            if not date:
                ret = field                         
            else:
                ret = field
#                ret=formatLang(field,date=True)
        return ret

    def myset(self, pair):
        if isinstance(pair, dict):
            self.localcontext['storage'].update(pair)
        return False

    def myget(self, key):
        if key in self.localcontext['storage'] and self.localcontext['storage'][key]:
            return self.localcontext['storage'][key]
        return False

   # Commercial name
    def commercial_name(self, partner_id, product_id, context=None):
        if not partner_id or not product_id:
            return []
        seller_ids = product_id.seller_ids
        if not isinstance(seller_ids, list):
            seller_ids = [seller_ids]
        ret = ''
        
        for seller in seller_ids:
            if seller.name == partner_id:
                ret = seller.product_name
        return ret    



   # Ingredients e ingredient, other name y other names
    def cqqs(self, obj, ing_type=False, only_main_ing=True, context=None):
        cqq_ids = obj.cqq_ids
        if not cqq_ids:
            return []
        if not isinstance(cqq_ids, list):
            cqq_ids = [cqq_ids]
        ret = []
        
        for cqq in cqq_ids:
            if not ing_type or cqq.ingredient_id.type == ing_type:
                if not only_main_ing or cqq.main_ingredient:                
                    ret.append(cqq)
        return ret    

    def cqq(self, obj, ing_type, context=None):
        ret = self.cqqs(obj, ing_type, context=context)
        if not ret:
            return False
        else:
            return ret[0]


    def ing_other_names(self, ingredient, other_name_type=False, context=None):
        ingredient_other_name_ids = ingredient.ingredient_other_name_ids
        if not ingredient_other_name_ids:
            return []
        if not isinstance(ingredient_other_name_ids, list):
            ingredient_other_name_ids = [ingredient_other_name_ids]
        ret = []
        
        for other_name in ingredient_other_name_ids:
            if not other_name_type or other_name.ingredient_name_category_id.name == other_name_type:
                ret.append(other_name)
        return ret  

   # Taxes y tax
    def taxes(self, obj, category=False, state=False,
                                    partner_ref=False, context=None):
        tax_ids = obj.tax_ids
        if not tax_ids:
            return []
        if not isinstance(tax_ids, list):
            tax_ids = [tax_ids]
        ret = []
        
        for tax in tax_ids:
            if not category or tax.document_category_id.name == category or tax.document_category_id.ref == category:
                if not state or tax.state == state:
                    if not partner_ref or tax.government_agency_id.ref == partner_ref:
                        ret.append(tax)
        return ret    

    def tax(self, obj, category=False, state=False,
                                    partner_ref=False, context=None):
        ret = self.taxes(obj, category=category, state=state, 
                                    partner_ref=partner_ref, context=context)
        if not ret:
            return False
        else:
            return ret[0]

   # Studies y study
    def studies(self, obj, category_name, state=False,
                                    laboratory_id=False, supplier_id=False, product_id=False, context=None):
        study_presentation_ids = obj.study_presentation_ids
        if not study_presentation_ids:
            return []
        if not isinstance(study_presentation_ids, list):
            study_presentation_ids = [study_presentation_ids]
        ret = []
        
        for study_presentation in study_presentation_ids:
            if study_presentation.document_category_id.reference == category_name or study_presentation.document_category_id.name == category_name:
                if not state or study_presentation.state == state:
                    if not laboratory_id or study_presentation.study_id.laboratory_id == laboratory_id:
                        if not supplier_id or study_presentation.study_id.supplier_id == supplier_id:
                            if not product_id or study_presentation.study_id.product_id == product_id:
                                ret.append(study_presentation.study_id)
        return ret    

    def study(self, obj, category_name, state=False,
                                    laboratory_id=False, supplier_id=False, product_id=False, context=None):
        ret = self.studies(obj, category_name, state=state, 
                                    laboratory_id=laboratory_id, supplier_id=supplier_id, product_id=product_id, context=context)
        if not ret:
            return False
        else:
            return ret[0]


   # Partner Documents y Partner document
    def p_docs(self, obj, category_name, state=False,
                                    partner_id=False, context=None):
        if not context:
            context = {}
        context['lang'] = ['en_US']
        partner_document_presentation_ids = obj.partner_document_presentation_ids
        if not partner_document_presentation_ids:
            return []
        if not isinstance(partner_document_presentation_ids, list):
            partner_document_presentation_ids = [partner_document_presentation_ids]
        ret = []
        
        for partner_document_presentation in partner_document_presentation_ids:
            if partner_document_presentation.document_category_id.name == category_name or partner_document_presentation.document_category_id.reference == category_name:
                if not state or partner_document_presentation.state == state:
                    if not partner_id or partner_document_presentation.partner_document_id.partner_id == partner_id:
                        ret.append(partner_document_presentation.partner_document_id)
        return ret    

    def p_doc(self, obj, category_name, state=False,
                                    partner_id=False, context=None):
        ret = self.p_docs(obj, category_name, state=state, partner_id=partner_id, context=context)
        if not ret:
            return False
        else:
            return ret[0]

    # Informations e information
    def informations(self, obj, category_name, state=False, partner_id=False, product_id=False, context=None):
        information_presentation_ids = obj.information_presentation_ids
        if not information_presentation_ids:
            return []
        if not isinstance(information_presentation_ids, list):
            information_presentation_ids = [information_presentation_ids]
        ret = []
        
        for information in information_presentation_ids:
            if information.information_category_id.name == category_name:
                if not state or information.state == state:
                    if not partner_id or information.parent_information_id.partner_id == partner_id:
                        if information.parent_information_id:
                            ret.append(information.parent_information_id.text)
                        else:
                            ret.append(information.text)                        
        return ret
    
    def information(self, obj, category_name, state=False, partner_id=False, product_id=False, context=None):
        ret = self.informations(obj, category_name, state=state, partner_id=partner_id, product_id=product_id, context=context)
        if not ret:
            return False
        else:
            return ret[0]        

    # processes y procces
    def processes(self, obj, partner_name, state=False, context=None):
        registry_process_ids = obj.registry_process_ids
        if not registry_process_ids:
            return []
        if not isinstance(registry_process_ids, list):
            registry_process_ids = [registry_process_ids]
        ret = []
        
        for registry in registry_process_ids:
            if registry.government_agency_id.ref == partner_name:
                if not state:
                    ret.append(registry)
                else:
                    if registry.state == state:
                        ret.append(registry)
        return ret
    
    def process(self, obj, partner_name, state=False, context=None):
        ret = self.processes(obj, partner_name, state=state, context=context)
        if not ret:
            return False
        else:
            return ret[0]

    # Partner Role in Registry
    def partners(self, obj, reg_type, context=None):
        partner_role_in_registry_list = obj.partner_role_in_registry_ids
        if not partner_role_in_registry_list:
            return []
        if not isinstance(partner_role_in_registry_list, list):
            partner_role_in_registry_list = [partner_role_in_registry_list]
        ret = []
        
        for partner_role_in_registry in partner_role_in_registry_list:
            if partner_role_in_registry.type == reg_type:
                ret.append(partner_role_in_registry.partner_id)
        return ret
    
    def partner(self, obj, reg_type, context=None):
        ret = self.partners(obj, reg_type, context=context)
        if not ret:
            return False
        else:
            return ret[0]


# Otras funciones genericas
    # Partner
    def format_partner_address(self, partner, context=None):
        ret = ''
        if partner.street:
            ret += partner.street
        if partner.street2:
            if partner.street:
                ret += ' - ' + partner.street2
            else:
                ret += partner.street2
        if ret != '':
            ret += '. '
        
        if partner.zip:
            ret += '(' + partner.zip + ')'
        if partner.city:
            if partner.zip:
                ret += ' ' + partner.city
            else:
                ret += partner.city
        if partner.state_id:
            if partner.city:
                ret += ' - ' + partner.state_id.name
            else:
                ret += partner.state_id.name
        if partner.zip or partner.city or partner.state_id:
            ret += '. '
        
        if partner.country_id:
            ret += partner.country_id.name + '.'
        
        return ret
    
    
    # Datetime
    def today(self, context=None):
        return date.today()
        
    def today_formated(self, context=None):
        return date.today().strftime('%d %m %Y')
    
    




#Funciones que se mantienen por compatibilidad hacia atras
    # Documents (lo dejamos por compatibilidad con reportes que ya se habian hecho)
    def filter_doc_presentations(self, partner_document_presentation_ids, category_name, state_name=False, context=None):
        if not partner_document_presentation_ids:
            return []
        if not isinstance(partner_document_presentation_ids, list):
            partner_document_presentation_ids = [partner_document_presentation_ids]
        ret = []
        
        for presentation in partner_document_presentation_ids:
            if presentation.document_category_id.name == category_name:
                if not state_name:
                    ret.append(presentation)
                else:
                    if presentation.state == state_name:
                        ret.append(presentation)
        return ret
    
    def get_one_doc_presentation(self, partner_document_presentation_ids, category_name, state_name=False, context=None):
        ret = self.filter_doc_presentations(partner_document_presentation_ids, category_name, state_name=state_name, context=context)
        if not ret:
            return False
        else:
            return ret[0]

    # Information (lo dejamos por compatibilidad hacia atras)
    def filter_inf_presentations(self, information_presentation_ids, category_name, state_name=False, context=None):
        if not information_presentation_ids:
            return []
        if not isinstance(information_presentation_ids, list):
            information_presentation_ids = [information_presentation_ids]
        ret = []
        
        for presentation in information_presentation_ids:
            if presentation.information_category_id.name == category_name:
                if not state_name:
                    ret.append(presentation)
                else:
                    if presentation.state == state_name:
                        ret.append(presentation)
        return ret
    
    def get_one_inf_presentation(self, information_presentation_ids, category_name, state_name=False, context=None):
        ret = self.filter_inf_presentations(information_presentation_ids, category_name, state_name=state_name, context=context)
        if not ret:
            return False
        else:
            return ret[0]    
    
    # Processes
    def filter_processes(self, registry_process_ids, partner_name, state_name=False, context=None):
        if not registry_process_ids:
            return []
        if not isinstance(registry_process_ids, list):
            registry_process_ids = [registry_process_ids]
        ret = []
        
        for registry in registry_process_ids:
            if registry.government_agency_id.ref == partner_name:
                if not state_name:
                    ret.append(registry)
                else:
                    if registry.state == state_name:
                        ret.append(registry)
        return ret
    
    def get_one_process(self, registry_process_ids, partner_name, state_name=False, context=None):
        ret = self.filter_processes(registry_process_ids, partner_name, state_name=state_name, context=context)
        if not ret:
            return False
        else:
            return ret[0]
    
    

    # Partner Role in Registry
    def filter_registries(self, partner_role_in_registry_list, reg_type, context=None):
        if not partner_role_in_registry_list:
            return []
        if not isinstance(partner_role_in_registry_list, list):
            partner_role_in_registry_list = [partner_role_in_registry_list]
        ret = []
        
        for partner_role_in_registry in partner_role_in_registry_list:
            if partner_role_in_registry.type == reg_type:
                ret.append(partner_role_in_registry)
        return ret
    
    def get_one_registry(self, partner_role_in_registry_list, reg_type, context=None):
        ret = self.filter_registries(partner_role_in_registry_list, reg_type, context=context)
        if not ret:
            return False
        else:
            return ret[0]

