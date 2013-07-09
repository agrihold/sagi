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

class technical_product_registry_report_wizard(osv.osv_memory):
    _name = 'technical_product_registry_report_wizard'
    _description = 'technical_product_registry_report_wizard'
    
    _columns = {
        'technical_product_id': fields.many2one('product.product', string='Technical Product', required=True, context={'default_function_type':'technical'}, domain=[('function_type','=','technical')]),
    }

    def generate_report_technical(self, cr, uid, ids, context=None):
        wizard = self.browse(cr, uid, ids)[0]
        
        product = wizard.technical_product_id.id
        if not product:
            return {'type': 'ir.actions.act_window_close'}
        context['technical_product_id'] = product
        
        result = {'type' : 'ir.actions.report.xml',
                  'context' : context,
                  'report_name': 'technical_product_registry_report',}
        return result










