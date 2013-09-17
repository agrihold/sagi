# -*- coding: utf-8 -*-
##############################################################################
#
#    SGR
#    Copyright (C) 2013 Grupo ADHOC
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


import re
import netsvc
from osv import osv, fields

class sample_request(osv.osv):
    """"""
    
    _name = 'sgr.sample_request'
    _inherit = [ _name ]

    _columns = {
        'ret_remaining_amount': fields.related('product_in_ret_id', 'remaining_amount',
                    type='float', string='RET Remaining Amount', readonly=True),
        'copy_amount_uom_id': fields.related('amount_uom_id', type='many2one', relation='product.uom', string='UOM', readonly=True),        
        }

    def create(self, cr, uid, vals, context=None):
        if vals.get('name','/')=='/':
            vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'sample.request') or '/'
        return super(sample_request, self).create(cr, uid, vals, context=context)

    def onchange_ret(self, cr, uid, ids, product_in_ret_id, context=None):
        v = {}
        if product_in_ret_id:
            product_in_ret_obj = self.pool.get('sgr.product_in_ret')
            product_in_ret = product_in_ret_obj.browse(cr, uid, product_in_ret_id, context=context)
            
            if not product_in_ret:
                return {'value': v}
            
            if isinstance(product_in_ret, list):
                product_in_ret = product_in_ret[0]
            v['amount_uom_id'] = product_in_ret.amount_uom_id.id     
            v['copy_amount_uom_id'] = product_in_ret.amount_uom_id.id     
        else:
            v['amount_uom_id'] = False
            v['copy_amount_uom_id'] = False

        return {'value': v}                       

sample_request()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
