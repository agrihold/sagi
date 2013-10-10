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

class document(osv.osv):
    """"""
    
    _name = 'sgr.document'
    _description = 'document'

    _columns = {
        'sgr_partner_document_id': fields.one2many('sgr.partner_document', 'sgr_document_id', 'sgr.partner_document_id', 'Partner Documents', help=u""""""),
        'sgr_dossier_document_id': fields.one2many('sgr.dossier_document', 'sgr_document_id', 'sgr.dossier_document_id', 'Dossier Reports', help=u""""""),
        'sgr_study_id': fields.one2many('sgr.study', 'sgr_document_id', 'sgr.study_id', 'Studies', help=u""""""),
        'sgr_tax_id': fields.one2many('sgr.tax', 'sgr_document_id', 'sgr.tax_id', 'Taxes', help=u""""""),
        'name': fields.char(string='Name', readonly=True, required=True, size=256, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)], 'to_pay': [('readonly', False)]}),
        'reference': fields.char(string='Reference', readonly=True, size=42, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)], 'to_pay': [('readonly', False)]}),
        'reviser_id': fields.many2one('res.partner', string='Reviser', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)], 'to_pay': [('readonly', False)]}),
        'approval_date': fields.date(string='Approval Date', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)], 'to_pay': [('readonly', False)]}),
        'expiration_date': fields.date(string='Expiration Date', readonly=True, states={'draft': [('readonly', False)], 'contracted': [('readonly', False)], 'sp_approved': [('readonly', False)], 'received': [('readonly', False)], 'requested': [('readonly', False)], 'to_pay': [('readonly', False)]}),
        'note': fields.text(string='Note', size=1024),
        'company_id': fields.many2one('res.company', string='Company'),
        'number_of_pages': fields.integer(string='Number of Pages'),
        'consularization_date': fields.date(string='Consularization Date'),
        'translation_date': fields.date(string='Translation Date'),
        'authentication_date': fields.date(string='Authentication Date'),
        'issue_date': fields.date(string='Issue Date'),
        'document_category_id': fields.many2one('sgr.document_category', string='Category', readonly=True, states={'draft': [('readonly', False)]}, domain=[('hierachical_type','=','normal')], required=True), 
        'information_ids': fields.one2many('sgr.information', 'document_id', string='information_ids'), 
        'move_ids': fields.one2many('sgr.document_move', 'document_id', string='Moves'), 
    }

    _defaults = {
        'company_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.document', context=c),
    }

    _order = "id desc"

    _constraints = [
    ]


    def get_default_company(self, cr, uid, ids, context=None):
        """"""
        raise NotImplementedError

    def do_approve(self, cr, uid, ids, context=None):
        """"""
        raise NotImplementedError

    def do_depreciate(self, cr, uid, ids, context=None):
        """"""
        raise NotImplementedError



document()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
