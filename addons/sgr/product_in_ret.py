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
from openerp import netsvc
from openerp.osv import osv, fields

class product_in_ret(osv.osv):
    """"""
    
    _name = 'sgr.product_in_ret'
    _description = 'product_in_ret'

    def _get_remaining_amount(self, cr, uid, ids, name, args, context=None):
        """"""
        raise NotImplementedError

    _columns = {
        'concentration': fields.float(string='Concentration'),
        'concentration_uom_id': fields.many2one('product.uom', string='Concentration UOM'),
        'amount_requested': fields.float(string='Requested', required=True),
        'amount_uom_id': fields.many2one('product.uom', string='Amount UOM', required=True),
        'amount_released': fields.float(string='Released'),
        'remaining_amount': fields.function(_get_remaining_amount, type='float', arg=None, fnct_inv_arg=None, obj=None, string='Remaining', readonly=True),
        'sample_request_ids': fields.one2many('sgr.sample_request', 'product_in_ret_id', string='Sample Request'), 
        'fromulated_product_registry_ids': fields.many2many('sgr.formulated_product_registry', 'sgr_product_in_ret_ids_fromulated_product_registry_ids_rel', 'product_in_ret_id', 'formulated_product_registry_id', string='fromulated_product_registry_ids'), 
        'technical_product_registry_ids': fields.many2many('sgr.technical_product_registry', 'sgr_product_in_ret_ids_technical_product_registry_ids_rel', 'product_in_ret_id', 'technical_product_registry_id', string='technical_product_registry_ids'), 
        'product_id': fields.many2one('product.product', string='Product', required=True), 
        'ret_registry_id': fields.many2one('sgr.ret_registry', string='Registry', ondelete='cascade', required=True), 
    }

    _defaults = {
    }


    _constraints = [
    ]


    def onchange_product(self, cr, uid, ids, product_id, context=None):
        """"""
        raise NotImplementedError



product_in_ret()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
