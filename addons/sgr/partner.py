# -*- coding: utf-8 -*-
##############################################################################
#
#    SGR
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
from openerp import netsvc
from openerp.osv import osv, fields

class partner(osv.osv):
    """"""
    
    _name = 'res.partner'
    _inherits = {  }
    _inherit = [ 'res.partner' ]

    _columns = {
        'is_laboratory': fields.boolean(string='Is Laboratory?'),
        'is_gov_agency': fields.boolean(string='Is Government Agency?'),
        'is_glp': fields.boolean(string='Is GLP?'),
        'gov_type': fields.selection([(u'state', u'State'), (u'federal', u'Federal')], string='Government Type'),
        'gov_registration_code': fields.char(string='Operating License Code'),
        'gov_registration_date': fields.date(string='Operating License Date'),
        'gov_registration_agency': fields.many2one('res.partner', string='Operating License Agency', context={'default_is_gov_agency':'True','default_is_company':'True'}, domain=[('is_gov_agency','=',True)]),
        'env_registration_code': fields.char(string='Env. Reg Code'),
        'env_registration_date': fields.date(string='Env. Reg Date'),
        'env_registration_agency': fields.many2one('res.partner', string='Env. Reg Agency', context={'default_is_gov_agency':'True','default_is_company':'True'}, domain=[('is_gov_agency','=',True)]),
        'state_registration_code': fields.char(string='State Registration Code', size=64),
        'state_registration_date': fields.date(string='State Registration Date'),
        'state_registration_agency': fields.many2one('res.partner', string='State Registration Agency', context={'default_is_gov_agency':'True','default_is_company':'True'}, domain=[('is_gov_agency','=',True)]),
        'vat': fields.char(string='VAT', size=64),
        'emergency_phone': fields.char(string='Emergency Phone', size=64),
        'proposal_as_sponsor_ids': fields.many2many('sgr.proposal', 'sgr_sponsor_ids_proposal_as_sponsor_ids_rel', 'partner_id', 'proposal_id', string='proposal_as_sponsor_ids'), 
        'ret_registry_sup_ids': fields.many2many('sgr.ret_registry', 'sgr_ret_registry_sup_ids_supplier_ids_rel', 'partner_id', 'ret_registry_id', string='ret_registry_sup_ids'), 
        'analytic_account_id': fields.many2one('account.analytic.account', string='Account and Contracts', help=u"""Este campo debe ser solo para partners del tipo laboratorios. Se debe crear automáticamente al crear un laboratorio una cuenta analitica del tipo &quot;view&quot;. Si se destilda el campo &quot;laboratorio&quot; al partner, borramos la cuenta?""", readonly=True), 
        'ret_registry_lab_ids': fields.many2many('sgr.ret_registry', 'sgr_laboratory_ids_ret_registry_lab_ids_rel', 'partner_id', 'ret_registry_id', string='ret_registry_lab_ids'), 
        'component_registry_detail_id': fields.many2many('sgr.component_registry_detail', 'sgr___supplier_ids_rel', 'partner_id', 'component_registry_detail_id', string='&lt;no label&gt;'), 
    }

    _defaults = {
    }


    _constraints = [
    ]


    def get_default_company(self, cr, uid, ids, context=None):
        """if is_gov_agency then company_id := res.user.company_id"""
        raise NotImplementedError

    def create_analytic_account(self, cr, uid, ids, context=None):
        """para los campos tipo laboratorio se debe crear una cuenta analitica tipo view, luego las cuentas de los contratos de ese laboratorio deben ser hijas de esta cuenta"""
        raise NotImplementedError



partner()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
