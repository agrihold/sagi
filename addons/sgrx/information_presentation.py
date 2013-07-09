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

class information_presentation(osv.osv):
    """"""
    _name = 'sgr.information_presentation'
    _inherit = [ _name ]

    def convert_to_information(self, cr, uid, ids, context=None):
        """analogo a los productos en una nota de venta. Cuando en un registor se agrega una informacion, se trae el texto de la misma que puede ser modificado por el usuario en esa informacion. A su vez puede existir una información en un registro sin tener asociada una información"""
        raise NotImplementedError

    def onchange_parent_information(self, cr, uid, ids, parent_information_id, context=None):
        """"""
        context = context or {}
        information_obj = self.pool.get('sgr.information')
        v = information_obj.read(cr, uid, product_id, ['text'])
        return {
            'value':  {
                'text': v['text'],
            }
        }


information_presentation()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
