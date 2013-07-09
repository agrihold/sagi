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

class communication(osv.Model):
    _inherit = 'sgr.communication'
    
    def send_alerts(self, cr, uid, context=None):
        self.send_alerts_with_upcoming_days(cr, uid, 2, context=context)
        
    def send_alerts_with_upcoming_days(self, cr, uid, upcoming_days, context=None):
        now = datetime.now()
        now_plus_upcoming_days = now + timedelta(days=upcoming_days)
        
        communication_resolving_ids = self.search(cr, uid, [('state','=','resolving_request')], context=context)
        communication_term_date_soon = []
        
        communications_due = []
        overdue_communications = []
            
        for communication in self.browse(cr, uid, communication_resolving_ids, context=context):
            if not communication.term_date:
                continue
            
            term_date = datetime.strptime(communication.term_date, date_format)
            
            if term_date <= now:
                overdue_communications.append(communication)
            elif now < term_date and term_date <= now_plus_upcoming_days:
                communications_due.append(communication)
        
        base_url = self.pool.get('ir.config_parameter').get_param(cr, 1, 'web.base.url')
        action_id = self.pool.get('ir.model.data').get_object_reference(cr, 1, 'sgr', 'view_sgr_formulated_product_registry_tree')[1]
        
        action_pool = self.pool.get('ir.actions.actions')
        action_id = action_pool.search(cr, uid, [('name', '=', 'Formulated Products Registrations')], context=context)
        if isinstance(action_id, list):
            action_id = action_id[0]
        
        for communication in communications_due:
            body = 'Official letter reply deadline soon: '
            body += self.generate_link_for_alert(cr, uid, base_url, communication, action_id, context=context)
            self.message_post(cr, uid, [communication.id], body=body, subtype="sgr_alerts.mt_communication_term_date_soon", context=context)
        
        for communication in overdue_communications:
            body = 'Official letter reply deadline expired: '
            body += self.generate_link_for_alert(cr, uid, base_url, communication, action_id, context=context)
            self.message_post(cr, uid, [communication.id], body=body, subtype="sgr_alerts.mt_communication_due", context=context)
            
        #all_tax_ids = selcommunicationf.search(cr, uid, [], context=context)
        #for tax in self.browse(cr, uid, all_tax_ids, context=context):
        #    print 'tax: ' + str(tax.id)
        #    self.message_post(cr, uid, [tax.id], body="Due Date Soon", subtype="sgr_alerts.mt_tax_due_date_soon", context=context)
        
            
        return True
    
    def generate_link_for_alert(self, cr, uid, base_url, communication, action_id, context=None):
        formulated_product_obj = self.pool.get('sgr.formulated_product_registry')
        filters = [('sgr_registry_id', '=',communication.registry_id.id)]
        formulated_product_id = formulated_product_obj.search(cr, uid, filters, context=context)
        if not formulated_product_id:
            return ''
        if isinstance(formulated_product_id, list):
            formulated_product_id = formulated_product_id[0]
        
        link = '<a href="' + base_url + '/?#action=' + str(action_id) + '&id=' + str(formulated_product_id) + '&view_type=form&model=sgr.formulated_product_registry">'
        link += communication.registry_id.computed_name
        link += '</a>'
        return link
        
    
    
communication()



