# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Business Applications
#    Copyright (C) 2004-2012 OpenERP S.A. (<http://openerp.com>).
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

from openerp.osv import fields, osv
from openerp.tools.translate import _

class agronomic_class(osv.osv):
    _inherit = 'sgr.agronomic_class'
    
    _columns = {
        'sequence_id': fields.many2one('ir.sequence', 'Sequence'),
        'code': fields.char('Code', size=2, required=True),
    }
    
    def create(self, cr, uid, vals, context=None):
        sequence_obj = self.pool.get('ir.sequence')
        seq_vals = {}
        seq_vals['name'] = 'agronomic_class: ' + vals['name']
        seq_vals['prefix'] = '%(y)s' + vals['code']
        seq_vals['suffix'] = 'G'
        seq_vals['padding'] = 3
        sequence_id = sequence_obj.create(cr, uid, seq_vals, context=context)
        
        vals['sequence_id'] = sequence_id
        return super(agronomic_class, self).create(cr, uid, vals, context=context)
    
    def write(self, cr, uid, ids, vals, context=None):
        ret = super(agronomic_class, self).write(cr, uid, ids, vals, context=context)
        
        sequence_obj = self.pool.get('ir.sequence')
        
        for agro_class in self.browse(cr, uid, ids, context=context):
            if not agro_class.sequence_id:
                self.create_sequence(cr, uid, [agro_class.id], context=context)
            
            else:
                seq_vals = {}
                if 'code' in vals:
                    seq_vals['prefix'] = '%(y)s' + vals['code']
                if 'name' in vals:
                    seq_vals['name'] = 'agronomic_class: ' + vals['name']
                if seq_vals:
                    if not isinstance(ids, list):
                        ids = [ids]
                    for ac in self.browse(cr, uid, ids, context=context):
                        sequence_obj.write(cr, uid, ac.sequence_id.id, seq_vals, context=context)
        return ret
    
    def create_sequence(self, cr, uid, ids, context=None):
        sequence_obj = self.pool.get('ir.sequence')
        
        for agro_class in self.browse(cr, uid, ids, context=context):
            seq_vals = {}
            seq_vals['name'] = 'agronomic_class: ' + agro_class.name
            seq_vals['prefix'] = '%(y)s' + agro_class.code
            seq_vals['suffix'] = 'G'
            seq_vals['padding'] = 3
            sequence_id = sequence_obj.create(cr, uid, seq_vals, context=context)
        
            vals = {}
            vals['sequence_id'] = sequence_id
            self.write(cr, uid, ids, vals, context=context)
    
    def write2(self, cr, uid, ids, vals, context=None):
        seq_vals = {}
        if 'code' in vals:
            seq_vals['prefix'] = '%(y)s' + vals['code']
        if 'name' in vals:
            seq_vals['prefix'] = 'agronomic_class: ' + vals['name']
        
        if seq_vals:
            sequence_obj = self.pool.get('ir.sequence')
            if not isinstance(ids, list):
                ids = [ids]
            for ac in self.browse(cr, uid, ids, context=context):
                sequence_obj.write(cr, uid, ac.sequence_id.id, seq_vals, context=context)
        
        ret = super(agronomic_class, self).write(cr, uid, ids, vals, context=context)
        
agronomic_class()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
