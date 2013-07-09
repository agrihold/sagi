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

class project(osv.osv):
    _inherit = 'project.project'
    
    def duplicate_template(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        context['duplicate_template'] = True
        return super(project, self).duplicate_template(cr, uid, ids, context=context)
    
    def copy(self, cr, uid, id, default=None, context=None):
        if context is None:
            context = {}
        
        back_to_draft = False
        if context.get('duplicate_template', False):
            back_to_draft = True
        
        ret = super(project, self).copy(cr, uid, id, default=default, context=context)
        
        if back_to_draft:
            self.set_draft(cr, uid, [ret], context=context)
        return ret

project()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
