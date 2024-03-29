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

class proposal_product(osv.osv):
    """"""
    _name = 'sgr.proposal_product'
    _inherit = [ _name ]

    def _get_sub_total(self, cr, uid, ids, names, args, context=None):
        """"""
        v = {}
        for pp in self.browse(cr, uid, ids):
            v[pp.id] = sum( ps.amount for ps in pp.product_study_ids )

        return v

    _columns = {
        'sub_total': fields.function(_get_sub_total, store=True, type='float', arg=None, fnct_inv_arg=None, obj=None, string='Subtotal', readonly=True),
    }

proposal_product()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
