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

class product_study(osv.osv):
    """"""
    
    _name = 'sgr.product_study'
    _description = 'product_study'

    _columns = {
        'term_days': fields.integer(string='Term (days)', required=True),
        'amount': fields.float(string='Amount'),
        'is_gpl': fields.boolean(string='Is GPL?'),
        'is_pretest': fields.boolean(string='Is Pretest?'),
        'sample_quantity': fields.float(string='Sample Quantity'),
        'sample_uom': fields.many2one('product.uom', string='Sample UOM'),
        'note': fields.text(string='Note'),
        'proposal_product_id': fields.many2one('sgr.proposal_product', string='proposal_product_id', ondelete='cascade', required=True), 
        'study_category_id': fields.many2one('sgr.document_category', string='Category', help=u"""Filtrar por categorías que sean del tipo de documento &quot;study&quot;""", required=True), 
        'study_id': fields.many2one('sgr.study', string='study_id'), 
        'batch_number_id': fields.many2many('stock.production.lot', 'sgr_product_study_ids_batch_number_id_rel', 'product_study_id', 'production_lot_id', string='Batchs Numbers'), 
        'lang_id': fields.many2many('res.lang', 'sgr_lang_id_product_study_ids_rel', 'product_study_id', 'lang_id', string='Languages', required=True), 
    }

    _defaults = {
    }


    _constraints = [
    ]




product_study()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
