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

class registry(osv.osv):
    """Si el registro es una modificación entonces se debe seleccionar un "operate_id"
Si un registro es del tipo operation "replacement", también se debe seleccionar un registro "operate_id" pero para validar el segundo registor el primero debe estar en estado expirado"""
    
    _name = 'sgr.registry'
    _description = 'Si el registro es una modificación entonces se debe seleccionar '

    _states_ = [
        # State machine: registry
        ('draft','Draft'),
        ('requested','Requested'),
        ('approved','Approved'),
        ('rejected','Rejected'),
        ('depreciated','Depreciated'),
        ('cancelled','Cancelled'),
    ]
    _columns = {
        'sgr_trademark_registry_id': fields.one2many('sgr.trademark_registry', 'sgr_registry_id', 'sgr.trademark_registry_id', 'Trademark Registrations', help=u""""""),
        'sgr_state_registry_id': fields.one2many('sgr.state_registry', 'sgr_registry_id', 'sgr.state_registry_id', 'State Registries', help=u""""""),
        'sgr_component_registry_id': fields.one2many('sgr.component_registry', 'sgr_registry_id', 'sgr.component_registry_id', 'Components Registries', help=u""""""),
        'sgr_technical_product_registry_id': fields.one2many('sgr.technical_product_registry', 'sgr_registry_id', 'sgr.technical_product_registry_id', 'Techinical Products Registries', help=u""""""),
        'sgr_laboratory_registry_id': fields.one2many('sgr.laboratory_registry', 'sgr_registry_id', 'sgr.laboratory_registry_id', 'Laboratories Registries', help=u""""""),
        'sgr_ret_registry_id': fields.one2many('sgr.ret_registry', 'sgr_registry_id', 'sgr.ret_registry_id', 'RET Registries', help=u""""""),
        'sgr_formulated_product_registry_id': fields.one2many('sgr.formulated_product_registry', 'sgr_registry_id', 'sgr.formulated_product_registry_id', 'Formulated Product Registries', help=u""""""),
        'type': fields.selection([(u'state', u'State'), (u'laboratory', u'Laboratory'), (u'component', u'Component'), (u'ret', u'RET'), (u'technical_product', u'Technical Product'), (u'formulated_product', u'Formulated Product'), (u'trademark', u'Trademark')], string='Type'),
        'registry_number': fields.char(string='Registry Number', readonly=True, size=64, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'operative_id': fields.many2one('res.company', string='Operative', readonly=True, required=True, states={'draft': [('readonly', False)]}),
        'proxy_id': fields.many2one('res.partner', string='Legal Representative', readonly=True, required=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}, context={'default_is_company':False}, domain=[('is_company','=',False)]),
        'project_id': fields.many2one('project.project', string='Project'),
        'company_id': fields.many2one('res.company', string='Company', required=True),
        'registry_date': fields.date(string='Registry Date', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'registry_expiration_date': fields.date(string='Registry Expiration Date', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'free_sale_number': fields.char(string='Free Sale Number', readonly=True, size=64, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'free_sale_date': fields.date(string='Free Sale Date', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'free_sale_expiration_date': fields.date(string='Free Sale Expiration Date', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}),
        'note': fields.text(string='Note'),
        'expected_date': fields.date(string='Expected Date'),
        'state': fields.selection(_states_, "State"),
        'communication_ids': fields.one2many('sgr.communication', 'registry_id', string='Communications'), 
        'partner_document_presentation_ids': fields.one2many('sgr.partner_document_presentation', 'registry_id', string='Partner Documents', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
        'registry_process_ids': fields.one2many('sgr.registry_process', 'registry_id', string='Processes', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
        'publications_ids': fields.one2many('sgr.publication', 'registry_id', string='Publications'), 
        'registry_category_id': fields.many2one('sgr.registry_category', string='Category', required=True), 
        'dossier_document_ids': fields.one2many('sgr.dossier_document', 'registry_id', string='Dossier Documents'), 
        'information_category_ids': fields.related(
                    'registry_category_id',
                    'information_category_ids',
                    type='many2many',
                    relation='sgr.registry_category',
                    string='information_category_ids'
                    ),
        'tax_ids': fields.one2many('sgr.tax', 'registry_id', string='Taxes'), 
        'study_presentation_ids': fields.one2many('sgr.study_presentation', 'registry_id', string='Studies'), 
        'information_presentation_ids': fields.one2many('sgr.information_presentation', 'registry_id', string='Informations', readonly=True, states={'draft': [('readonly', False)], 'requested': [('readonly', False)]}), 
    }

    _defaults = {
        'state': 'draft',
        'type': lambda self, cr, uid, context=None: context and context.get('type', False),
        'operative_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.registry', context=c),
        'company_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.registry', context=c),
    }

    _order = "id desc"

    _constraints = [
    ]


    def get_registro_types(self, cr, uid, ids, context=None):
        """"""
        raise NotImplementedError

    def create_new(self, cr, uid, ids, context=None):
        """"""
        raise NotImplementedError

    def onchange_registry_category(self, cr, uid, ids, registry_category_id, context=None):
        """"""
        raise NotImplementedError

    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'sgr.registry', obj_id, cr)
            wf_service.trg_create(uid, 'sgr.registry', obj_id, cr)
        return True



registry()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
