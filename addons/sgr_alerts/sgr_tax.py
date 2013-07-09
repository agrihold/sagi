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

class tax(osv.Model):
    _inherit = 'sgr.tax'
    
    def send_alerts(self, cr, uid, context=None):
        self.send_alerts_with_upcoming_days(cr, uid, 2, context=context)
        
    def send_alerts_with_upcoming_days(self, cr, uid, upcoming_days, context=None):
        now = datetime.now()
        now_plus_upcoming_days = now + timedelta(days=upcoming_days)
        
        tax_to_paid_ids = self.search(cr, uid, [('state','=','to_pay')], context=context)
        tax_due_date_soon = []
        
        taxs_due = []
        overdue_taxs = []
            
        for tax in self.browse(cr, uid, tax_to_paid_ids, context=context):
            if not tax.approval_date:
                continue
            
            approval_date = datetime.strptime(tax.approval_date, date_format)
            
            if approval_date <= now:
                overdue_taxs.append(tax)
            elif now < approval_date and approval_date <= now_plus_upcoming_days:
                taxs_due.append(tax)
        
        for tax in taxs_due:
            self.message_post(cr, uid, [tax.id], body="Tax payment deadline soon", subtype="sgr_alerts.mt_tax_due_date_soon", context=context)
        
        for tax in overdue_taxs:
            self.message_post(cr, uid, [tax.id], body="Tax payment deadline expired", subtype="sgr_alerts.mt_tax_due_date", context=context)
            
        #all_tax_ids = self.search(cr, uid, [], context=context)
        #for tax in self.browse(cr, uid, all_tax_ids, context=context):
        #    print 'tax: ' + str(tax.id)
        #    self.message_post(cr, uid, [tax.id], body="Due Date Soon", subtype="sgr_alerts.mt_tax_due_date_soon", context=context)
        
            
        return True
        
    
    
tax()



