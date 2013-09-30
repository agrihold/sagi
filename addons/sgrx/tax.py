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

class tax(osv.osv):
    _name = 'sgr.tax'
    _inherit = 'sgr.tax'
    
    _columns = {
        # 'document_category_id': fields.many2one('sgr.document_category', string='Category', required=True, context={'default_type':'tax'}, domain=[('type','=','tax')]),
    }

    def _get_currency(self, cr, uid, ctx):
        comp = self.pool.get('res.users').browse(cr,uid,uid).company_id
        if not comp:
            comp_id = self.pool.get('res.company').search(cr, uid, [])[0]
            comp = self.pool.get('res.company').browse(cr, uid, comp_id)
        return comp.currency_id.id    
    
    _defaults = {
        # "currency_id": 'BRL'
        "currency_id": _get_currency
    }

tax()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
