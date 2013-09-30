# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011 Eficent (<http://www.eficent.com/>)
#              Jordi Ballester Alomar <jordi.ballester@eficent.com>
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

import tools
from osv import fields, osv
from tools.translate import _

from datetime import datetime, timedelta

date_format = '%Y-%m-%d %H:%M:%S'

class res_users(osv.Model):
    _inherit = 'res.users'
    
    def send_all_alerts(self, cr, uid, ids, context=None):
        tax_obj = self.pool.get('sgr.tax')
        tax_obj.send_alerts(cr, uid, context=context)
        sample_request_obj = self.pool.get('sgr.sample_request')
        sample_request_obj.send_alerts(cr, uid, context=context)
        communication_obj = self.pool.get('sgr.communication')
        communication_obj.send_alerts(cr, uid, context=context)
        return True
    
res_users()



