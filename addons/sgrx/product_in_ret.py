# -*- coding: utf-8 -*-
##############################################################################
#
#    SGR. Sistema de Gestion de Registros
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

class product_in_ret(osv.osv):
    """"""
    _name = 'sgr.product_in_ret'
    _inherit = [ _name ]
#    _rec_name = 'product_id' 
#lo deshabilite para que se muestre bien en los sample request, hay que ver si sigue andando bien la busqueda

    def _get_remaining_amount(self, cr, uid, ids, name, args, context=None):
        """"""
        product_uom_obj = self.pool.get('product.uom')

        context = context or {}
        r = {}
        for pir in self.browse(cr, uid, ids, context=context):
            r[pir.id] = pir.amount_released - sum(
                product_uom_obj._compute_qty(cr, uid, sr.amount_uom_id.id, sr.amount, pir.amount_uom_id.id)
                for sr in pir.sample_request_ids
            )
        return r

    _columns = {
        'remaining_amount': fields.function(_get_remaining_amount, type='float', arg=None, fnct_inv_arg=None, obj=None, string='Remaining', readonly=True),
        'name': fields.related(
                    'ret_registry_id',
                    'name',
                    type='char',
                    relation='sgr.ret_registry',
                    string='name'
                    ),
    }

    def onchange_product(self, cr, uid, ids, product_id, context=None):
        """"""
        context = context or {}
        product_obj = self.pool.get('product.product')
        v = product_obj.read(cr, uid, product_id, ['uom_id'])
        return {
            'value':  {
                'amount_uom_id': v['uom_id'][0],
            }
        }


product_in_ret()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
