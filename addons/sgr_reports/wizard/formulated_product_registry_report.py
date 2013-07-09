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

import netsvc

from osv import fields, osv
import pooler

class formulated_product_registry_report_wizard(osv.osv_memory):
    _name = 'formulated_product_registry_report_wizard'
    _description = 'formulated_product_registry_report_wizard'
    
    _columns = {
        'formulated_product_id': fields.many2one('product.product', string='Formulated Product', required=True, context={'default_function_type':'formulated'}, domain=[('function_type','=','formulated')]),
    }

    def generate_report_formulated(self, cr, uid, ids, context=None):
        wizard = self.browse(cr, uid, ids)[0]
        
        product = wizard.formulated_product_id.id
        if not product:
            return {'type': 'ir.actions.act_window_close'}
        context['formulated_product_id'] = product
        
        result = {'type' : 'ir.actions.report.xml',
                  'context' : context,
                  'report_name': 'formulated_product_registry_report',}
        return result










