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

class partner(osv.osv):
    """"""
    _name = 'res.partner'
    _inherit = [ _name ]

    def create_analytic_account(self, cr, uid, ids, context=None):
        """para los campos tipo laboratorio se debe crear una cuenta analitica tipo view, luego las cuentas de los contratos de ese laboratorio deben ser hijas de esta cuenta"""
        context=context or {}
        analytic_obj = self.pool.get("account.analytic.account")
        for par in self.browser(cr, uid, ids):
            if par.is_laboratory and not par.analytic_account_id:
                # Busco la cuenta analitica pabre y la creo si no existe.
                import pdb; pdb.set_trace()
                #if analytic_obj.search(cr, uid, [('company_id','=',par.company_id),('')]):

                # Creo la cuenta analitica view.
                value = {
                    'name': par.name,
                    'complete_name': par.name,
                    #'code': , # Automatico
                    'type': 'view',
                    'template_id': False,
                    'description': '<- some description ->',
                    'parent_id': ala_par_id,
                    'partner_id': par.id,
                    'user_id': False,
                    'manager_id': False,
                    'date_start': False,
                    'company_id': False,
                    'state': 'open',
                    'currency_id': False,
                }
                ana_id = analytic_obj.create(cr, uid, value)
        return {}

partner()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
