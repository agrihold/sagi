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

class config_settings(osv.osv):
    """"""
    
    _name = 'sagi.config_settings'
    _description = 'config_settings'
    _inherits = {  }
    _inherit = [ 'res.config.settings' ]

    _columns = {
        'creation_duration': fields.integer(string='Creation Term (days)'),
        'snp_file': fields.binary(string='SNP'),
        'qnp_file': fields.binary(string='QNP'),
        'CIO_file': fields.binary(string='Operative Innovation Committee'),
        'summary_file': fields.binary(string='Summary'),
        'CO_file': fields.binary(string='Operational Committee'),
        'presentation_file': fields.binary(string='Presentation'),
        'CIA_file': fields.binary(string='CIA_file'),
        'charter_file': fields.binary(string='Project Charter'),
        'kick_off_ac_file': fields.binary(string='Critical Analysis Kick Off'),
        'ca_sc_file': fields.binary(string='Supply Chain'),
        'ca_sc_pred_term': fields.integer(string='Supply Chain default term (days)'),
        'ca_mkt_file': fields.binary(string='Marketing'),
        'ca_mkt_pred_term': fields.integer(string='Marketing default term (days)'),
        'ca_dr_file': fields.binary(string='Develp. and Registration'),
        'ca_dr_pred_term': fields.integer(string='Develp. and Registration default term (days)'),
        'ca_result_file': fields.binary(string='Result'),
        'ca_result_pred_term': fields.integer(string='Result default term (days)'),
        'planning_pred_term': fields.integer(string='Planning default term (days)'),
        'kick_off_project_file': fields.binary(string='Project Kick Off'),
        'closing_report_file': fields.binary(string='Closing Report'),
        'closing_pred_term': fields.integer(string='Closing default term (days)'),
    }

    _defaults = {
    }


    _constraints = [
    ]




config_settings()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
