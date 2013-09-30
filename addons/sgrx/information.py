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

class information(osv.osv):
    """"""
    _name = 'sgr.information'
    _inherit = [ _name ]

    def _get_name(self, cr, uid, ids, name, args, context=None):
        """se calcula como la categoría de la infomracion mas el nombre del producto o el nombre del partner"""
        v = {}
        info = self.read(cr, uid, ids, ['partner_id', 'product_id'])
        for i in info:
            v[i['id']] = ' - '.join([ i[f][1] for f in ['partner_id','product_id'] if i[f] ])
        return v

    _columns = {
        'name': fields.function(_get_name, store=True, type='char', arg=None, fnct_inv_arg=None, obj=None, string='Name', readonly=True, size=128),
    }
information()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
