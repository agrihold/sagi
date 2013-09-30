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
from res_config_parameters import *

class sagi_configuration(osv.TransientModel):
    _inherit = 'sagi.config_settings'
    
    _columns = {
        'property_template_project_id': fields.many2one('project.project', view_load=True, string='Template Project', domain=[('state', '=', 'template')]),
    }
    
    def get_default_property_template_project_id(self, cr, uid, ids, context=None):
        property_obj = self.pool.get('ir.property')
        prop_ids = property_obj.search(cr, uid, [('name', '=', 'property_template_project_id')], context=context)
        if prop_ids:
            prop = property_obj.browse(cr, uid, prop_ids[0], context=context)
            return {'property_template_project_id': prop.value_reference.id}
        return {'property_template_project_id': False}
    
    def set_property_template_project_id(self, cr, uid, ids, context=None):
        property_obj = self.pool.get('ir.property')
        prop_ids = property_obj.search(cr, uid, [('name', '=', 'property_template_project_id')], context=context)
        for record in self.browse(cr, uid, ids, context=context):
            if prop_ids:
                p_val = {}
                p_val['value'] = record['property_template_project_id'] or False
                property_obj.write(cr, uid, prop_ids, p_val, context=context)
                
            else:
                field_obj = self.pool.get('ir.model.fields')
                field_id = field_obj.search(cr, uid, [('name', '=', 'property_template_project_id')])
                if not field_id:
                    raise osv.except_osv(_('Field not found'), _('Field ' + 'property_template_project_id' + ' not found in the Database'))
                if isinstance(field_id, list):
                    field_id = field_id[0]
                
                project = record['property_template_project_id'] or False
                p_val = {}
                p_val['name'] = 'property_template_project_id'
                p_val['fields_id'] = field_id
                p_val['type'] = 'many2one'
                p_val['selection'] = 'ir.attachment'
                p_val['value'] = project
                property_obj.create(cr, uid, p_val, context=context)
                
    # Functions for setting and getting the integer parameters
    
    def default_get_int_function(self, cr, uid, ids, para_name, field_name, context=None):
        config_parameters = self.pool.get('ir.config_parameter')
        field_value = config_parameters.get_param(cr, uid, para_name, context=context)
        if field_value:
            return {field_name: int(field_value)}
        else:
            return {field_name: 0}
        
    def default_set_int_function(self, cr, uid, ids, para_name, field_name, context=None):
        config_parameters = self.pool.get('ir.config_parameter')
        for record in self.browse(cr, uid, ids, context=context):
            config_parameters.set_param(cr, uid, para_name, record[field_name] or '0', context=context)
        
    def get_default_creation_duration(self, cr, uid, ids, context=None):
        return self.default_get_int_function(cr, uid, ids, parameter_creation_duration, 'creation_duration', context=context)
    def set_creation_duration(self, cr, uid, ids, context=None):
        return self.default_set_int_function(cr, uid, ids, parameter_creation_duration, 'creation_duration', context=context)
    
    def get_default_ca_sc_pred_term(self, cr, uid, ids, context=None):
        return self.default_get_int_function(cr, uid, ids, parameter_ca_sc_pred_term, 'ca_sc_pred_term', context=context)
    def set_ca_sc_pred_term(self, cr, uid, ids, context=None):
        return self.default_set_int_function(cr, uid, ids, parameter_ca_sc_pred_term, 'ca_sc_pred_term', context=context)
    
    def get_default_ca_mkt_pred_term(self, cr, uid, ids, context=None):
        return self.default_get_int_function(cr, uid, ids, parameter_ca_mkt_pred_term, 'ca_mkt_pred_term', context=context)
    def set_ca_mkt_pred_term(self, cr, uid, ids, context=None):
        return self.default_set_int_function(cr, uid, ids, parameter_ca_mkt_pred_term, 'ca_mkt_pred_term', context=context)
    
    def get_default_ca_dr_pred_term(self, cr, uid, ids, context=None):
        return self.default_get_int_function(cr, uid, ids, parameter_ca_dr_pred_term, 'ca_dr_pred_term', context=context)
    def set_ca_dr_pred_term(self, cr, uid, ids, context=None):
        return self.default_set_int_function(cr, uid, ids, parameter_ca_dr_pred_term, 'ca_dr_pred_term', context=context)
    
    def get_default_ca_result_pred_term(self, cr, uid, ids, context=None):
        return self.default_get_int_function(cr, uid, ids, parameter_ca_result_pred_term, 'ca_result_pred_term', context=context)
    def set_ca_result_pred_term(self, cr, uid, ids, context=None):
        return self.default_set_int_function(cr, uid, ids, parameter_ca_result_pred_term, 'ca_result_pred_term', context=context)
    
    def get_default_planning_pred_term(self, cr, uid, ids, context=None):
        return self.default_get_int_function(cr, uid, ids, parameter_planning_pred_term, 'planning_pred_term', context=context)
    def set_planning_pred_term(self, cr, uid, ids, context=None):
        return self.default_set_int_function(cr, uid, ids, parameter_planning_pred_term, 'planning_pred_term', context=context)
    
    def get_default_closing_pred_term(self, cr, uid, ids, context=None):
        return self.default_get_int_function(cr, uid, ids, parameter_closing_pred_term, 'closing_pred_term', context=context)
    def set_closing_pred_term(self, cr, uid, ids, context=None):
        return self.default_set_int_function(cr, uid, ids, parameter_closing_pred_term, 'closing_pred_term', context=context)
    
    # Functions for setting and getting the files parameters
    
    def default_get_file_function(self, cr, uid, ids, ir_property_name, config_field_name, context=None):
        property_obj = self.pool.get('ir.property')
        prop_ids = property_obj.search(cr, uid, [('name', '=', ir_property_name)], context=context)
        if prop_ids:
            prop = property_obj.browse(cr, uid, prop_ids[0], context=context)
            attachment = prop.value_reference
            return {config_field_name: attachment.datas}
        return {config_field_name: False}
    
    def default_set_file_function(self, cr, uid, ids, ir_property_name, field_name, config_field_name, context=None):
        property_obj = self.pool.get('ir.property')
        attachment_obj = self.pool.get('ir.attachment')
        prop_ids = property_obj.search(cr, uid, [('name', '=', ir_property_name)], context=context)
        for record in self.browse(cr, uid, ids, context=context):
            if prop_ids:
                prop = property_obj.browse(cr, uid, prop_ids[0], context=context)
                attachment = prop.value_reference
                val = {'datas': record[config_field_name] or False}
                attachment_obj.write(cr, uid, [attachment.id], val, context=context)
            
            else:
                val = {}
                val['name'] = ir_property_name
                val['type'] = 'binary'
                val['datas'] = record[config_field_name] or False
                att_id = attachment_obj.create(cr, uid, val, context=context)
                attachment = attachment_obj.browse(cr, uid, att_id, context=context)
                if isinstance(attachment, list):
                    attachment = attachment[0]
                
                field_obj = self.pool.get('ir.model.fields')
                field_id = field_obj.search(cr, uid, [('name', '=', field_name)])
                if not field_id:
                    raise osv.except_osv(_('Field not found'), _('Field ' + field_name + ' not found in the Database'))
                if isinstance(field_id, list):
                    field_id = field_id[0]
                
                p_val = {}
                p_val['name'] = ir_property_name
                p_val['fields_id'] = field_id
                p_val['type'] = 'many2one'
                p_val['selection'] = 'ir.attachment'
                p_val['value'] = att_id
                property_obj.create(cr, uid, p_val, context=context)
    
    def get_default_snp_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, snp_file_attachment_ir_property, 'snp_file', context=context)
    def set_snp_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, snp_file_attachment_ir_property, snp_file_attachment_field,
                        'snp_file', context=context)
    
    def get_default_qnp_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, qnp_file_attachment_ir_property, 'qnp_file', context=context)
    def set_qnp_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, qnp_file_attachment_ir_property, qnp_file_attachment_field,
                        'qnp_file', context=context)
    
    def get_default_CIO_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, cio_file_attachment_ir_property, 'CIO_file', context=context)
    def set_CIO_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, cio_file_attachment_ir_property, cio_file_attachment_field,
                        'CIO_file', context=context)
    
    def get_default_summary_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, summary_file_attachment_ir_property, 'summary_file', context=context)
    def set_summary_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, summary_file_attachment_ir_property, summary_file_attachment_field,
                        'summary_file', context=context)
    
    def get_default_CO_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, co_file_attachment_ir_property, 'CO_file', context=context)
    def set_CO_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, co_file_attachment_ir_property, co_file_attachment_field,
                        'CO_file', context=context)
    
    def get_default_presentation_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, presentation_file_attachment_ir_property,
                        'presentation_file', context=context)
    def set_presentation_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, presentation_file_attachment_ir_property,
                        presentation_file_attachment_field, 'presentation_file', context=context)
    
    def get_default_CIA_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, cia_file_attachment_ir_property, 'CIA_file', context=context)
    def set_CIA_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, cia_file_attachment_ir_property, cia_file_attachment_field,
                        'CIA_file', context=context)
    
    def get_default_charter_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, charter_file_attachment_ir_property, 'charter_file', context=context)
    def set_charter_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, charter_file_attachment_ir_property, charter_file_attachment_field, 
                        'charter_file', context=context)
    
    def get_default_kick_off_ac_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, kick_off_ac_file_attachment_ir_property,
                        'kick_off_ac_file', context=context)
    def set_kick_off_ac_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, kick_off_ac_file_attachment_ir_property,
                        kick_off_ac_file_attachment_field, 'kick_off_ac_file', context=context)
    
    def get_default_ca_sc_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, ca_sc_file_attachment_ir_property, 'ca_sc_file', context=context)
    def set_ca_sc_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, ca_sc_file_attachment_ir_property, ca_sc_file_attachment_field, 
                        'ca_sc_file', context=context)
    
    def get_default_ca_mkt_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, ca_mkt_file_attachment_ir_property, 'ca_mkt_file', context=context)
    def set_ca_mkt_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, ca_mkt_file_attachment_ir_property, ca_mkt_file_attachment_field, 
                        'ca_mkt_file', context=context)
    
    def get_default_ca_dr_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, ca_dr_file_attachment_ir_property, 'ca_dr_file', context=context)
    def set_ca_dr_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, ca_dr_file_attachment_ir_property, ca_dr_file_attachment_field, 
                        'ca_dr_file', context=context)
    
    def get_default_ca_result_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, ca_result_file_attachment_ir_property, 'ca_result_file', context=context)
    def set_ca_result_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, ca_result_file_attachment_ir_property, ca_result_file_attachment_field, 
                        'ca_result_file', context=context)
    
    def get_default_kick_off_project_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, kick_off_project_file_attachment_ir_property,
                        'kick_off_project_file', context=context)
    def set_kick_off_project_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, kick_off_project_file_attachment_ir_property,
                        kick_off_project_file_attachment_field, 'kick_off_project_file', context=context)
    
    def get_default_closing_report_file(self, cr, uid, ids, context=None):
        return self.default_get_file_function(cr, uid, ids, closing_report_file_attachment_ir_property,
                        'closing_report_file', context=context)
    def set_closing_report_file(self, cr, uid, ids, context=None):
        return self.default_set_file_function(cr, uid, ids, closing_report_file_attachment_ir_property,
                        closing_report_file_attachment_field, 'closing_report_file', context=context)
    
sagi_configuration()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:





