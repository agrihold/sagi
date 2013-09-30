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

from osv import fields, osv
from tools.translate import _

class create_default_project(osv.osv_memory):
    _name = 'create_default_project'
    _description = 'Wizard to create default project'

    _columns = {
        'name': fields.char('Name', size=200, required=True),
        'code': fields.char('Code', size=200, required=True),
        'project_manager_id': fields.many2one('res.users', _('Project Manager'), required=True),
        'project_template_id': fields.many2one('project.project', _('Project Template'), required=True,
                                    domain=[('state','=','template')]),
        'new_product_project_id': fields.many2one('sagi.new_product_project', _('New Product Project')),
    }
    
    def _get_default_new_product_project_id(self, cr, uid, context=None):
        return context.get('active_id', False)
    
    def _get_default_name(self, cr, uid, context=None):
        active_id = context.get('active_id', False)
        if active_id:
            new_product_project_obj = self.pool.get('sagi.new_product_project')
            new_product_project = new_product_project_obj.browse(cr, uid, active_id, context=context)
            if isinstance(new_product_project, list):
                new_product_project = new_product_project[0]
            return new_product_project.name
        return False
    
    def _get_default_code(self, cr, uid, context=None):
        active_id = context.get('active_id', False)
        if active_id:
            new_product_project_obj = self.pool.get('sagi.new_product_project')
            new_product_project = new_product_project_obj.browse(cr, uid, active_id, context=context)
            if isinstance(new_product_project, list):
                new_product_project = new_product_project[0]
            code = new_product_project.reference
            if not code:
                return False
            else:
                return code[0:-1] + 'P'
        return False
    
    def _get_default_project_manager(self, cr, uid, context=None):
        active_id = context.get('active_id', False)
        if active_id:
            new_product_project_obj = self.pool.get('sagi.new_product_project')
            new_product_project = new_product_project_obj.browse(cr, uid, active_id, context=context)
            if isinstance(new_product_project, list):
                new_product_project = new_product_project[0]
            return new_product_project.project_leader.id
        return False
    
    def _get_default_project_template(self, cr, uid, context=None):
        property_obj = self.pool.get('ir.property')
        prop_ids = property_obj.search(cr, uid, [('name', '=', 'property_template_project_id')], context=context)
        if prop_ids:
            prop = property_obj.browse(cr, uid, prop_ids[0], context=context)
            return prop.value_reference.id
        return False
    
    _defaults = {
        'name': _get_default_name,
        'code': _get_default_code,
        'project_manager_id': _get_default_project_manager,
        'project_template_id': _get_default_project_template,
        'new_product_project_id': _get_default_new_product_project_id,
    }
    
    def view_init(self, cr, uid, fields_list, context=None):
        active_id = context.get('active_id', False)
        if active_id:
            new_product_project_obj = self.pool.get('sagi.new_product_project')
            new_product_project = new_product_project_obj.browse(cr, uid, active_id, context=context)
            if isinstance(new_product_project, list):
                new_product_project = new_product_project[0]
            if new_product_project.project:
                raise osv.except_osv(_('Project already defined'),
                                     _('There is already another project defined for this New Product Project.'))
        
        return super(create_default_project, self).view_init(cr, uid, fields_list, context=context)
        
    def generate_project(self, cr, uid, ids, context=None):
        wizard = self.browse(cr, uid, ids)[0]
        
        name = wizard.name
        code = wizard.code
        project_manager = wizard.project_manager_id
        project_template = wizard.project_template_id
        new_product_project = wizard.new_product_project_id
        
        project_obj = self.pool.get('project.project')
        duplicate_ret = project_obj.duplicate_template(cr, uid, [project_template.id], context=context)
        new_project_id = duplicate_ret.get('res_id', False)
        if not new_project_id:
            return False
        
        new_project_vals = {'name': name, 'code': code, 'user_id': project_manager.id}
        project_obj.write(cr, uid, new_project_id, new_project_vals, context=context)
        
        new_product_project_obj = self.pool.get('sagi.new_product_project')
        new_product_project_vals = {'project': new_project_id}
        new_product_project_obj.write(cr, uid, new_product_project.id, new_product_project_vals, context=context)
        
        '''
        categories = wizard.category_ids
        if not categories:
            return {'type': 'ir.actions.act_window_close'}
        if not isinstance(categories, list):
            categories = [categories]
        context['category_ids'] = map(lambda cat: cat.id, categories)
        
        pricelist_id = wizard.pricelist_id.id
        if isinstance(pricelist_id, list):
            pricelist_id = pricelist_id[0]
        context['pricelist_id'] = pricelist_id
        result = {'type' : 'ir.actions.report.xml',
                  'context' : context,
                  'report_name': 'report_product_catalog',}
        return result
        '''
        return True
create_default_project()
