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

date_format = '%Y-%m-%d'

class sample_request(osv.Model):
    _inherit = 'sgr.sample_request'
    
    def send_alerts(self, cr, uid, context=None):
        self.send_alerts_with_upcoming_days(cr, uid, 2, context=context)
        
    def send_alerts_with_upcoming_days(self, cr, uid, upcoming_days, context=None):
        now = datetime.now()
        now_plus_upcoming_days = now + timedelta(days=upcoming_days)
        
        sample_request_requested_ids = self.search(cr, uid, [('state','=','requested')], context=context)
        sample_request_deadline_soon = []
        
        sample_requests_due = []
        overdue_sample_resquests = []
            
        for sample_request in self.browse(cr, uid, sample_request_requested_ids, context=context):
            if not sample_request.deadline:
                continue
            
            deadline = datetime.strptime(sample_request.deadline, date_format)
            
            if deadline <= now:
                overdue_sample_resquests.append(sample_request)
            elif now < deadline and deadline <= now_plus_upcoming_days:
                sample_requests_due.append(sample_request)
        
        for sample_request in sample_requests_due:
            self.message_post(cr, uid, [sample_request.id], body="Sample delivery deadline soon", subtype="sgr_alerts.mt_sample_request_deadline_soon", context=context)
        
        for sample_request in overdue_sample_resquests:
            self.message_post(cr, uid, [sample_request.id], body="Sample delivery deadline expired", subtype="sgr_alerts.mt_sample_request_due", context=context)
            
        #all_tax_ids = selsample_requestf.search(cr, uid, [], context=context)
        #for tax in self.browse(cr, uid, all_tax_ids, context=context):
        #    print 'tax: ' + str(tax.id)
        #    self.message_post(cr, uid, [tax.id], body="Due Date Soon", subtype="sgr_alerts.mt_tax_due_date_soon", context=context)
        
            
        return True
        
    
    
sample_request()



