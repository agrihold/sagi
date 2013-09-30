# -*- coding: utf-8 -*-
##############################################################################
#
#    SAGI
#    Copyright (C) 2013 No author.
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
from openerp import netsvc
from openerp.osv import osv, fields

class npp_creation(osv.osv):
    """Hacer que se pueda seguir los cambios de estado (con mensajes)
Hacer que se pueda seguir si esta cerca de una next action"""
    
    _name = 'sagi.new_product_project'
    _inherits = {  }
    _inherit = [ 'sagi.new_product_project' ]

    _track = {
    }
    _columns = {
        'creation_date_to_start': fields.date(string='Date to Start'),
        'creation_date_to_end': fields.date(string='Date to End'),
        'creation_started_date': fields.date(string='Started Date'),
        'creation_end_date': fields.date(string='End Date'),
        'SNP_file': fields.binary(string='SNP', help=u"""Exigido para pasar a etapa &quot;snp presented&quot;"""),
        'QNP_file': fields.binary(string='QNP'),
        'CIO_file': fields.binary(string='Operative Innovation Committee'),
        'summary_file': fields.binary(string='Summary'),
        'CO_file': fields.binary(string='Operational Committee'),
        'presentation_file': fields.binary(string='Presentation'),
        'CIA_file': fields.binary(string='Agrihold Innovation Committee'),
        'date_to_end': fields.date(string='Expected End Date'),
        'budget': fields.float(string='Budjet (USD)'),
        'project_leader': fields.many2one('res.users', string='Project Leader'),
        'project_sponsor': fields.many2one('res.users', string='Project Sponsor'),
        'interested_operative_ids': fields.many2many('res.company', 'sagi___interested_operative_ids_rel', 'new_product_project_id', 'company_id', string='Interested Operatives'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




npp_creation()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
