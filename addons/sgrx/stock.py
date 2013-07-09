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

class stock_move(osv.osv):
    """"""
    _name = 'stock.move'
    _inherits = {  }
    _inherit = ['stock.move','mail.thread']
    _states_ = [
    ]
    _track = {
        'state': {
            'sgrx.mt_move_change"': lambda self, cr, uid, obj, ctx=None: obj['state'] in ['draft', 'cancel', 'waiting', 'confirmed', 'assigned', 'done'],
            #'sale.mt_order_sent': lambda self, cr, uid, obj, ctx=None: obj['state'] in ['sent']
        },
    }        
    _columns = {
        'sample_request_id': fields.many2one('sgr.sample_request', string='Sample Request'), 
        'note': fields.text(string='Note'), 
    }
    _defaults = {
    }


stock_move()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
