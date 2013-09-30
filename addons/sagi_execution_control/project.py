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

class project(osv.osv):
    _inherit = 'project.project'
    
    def compute_control_status(self, cr, uid, ids, context=None):
        ret = super(project, self).compute_control_status(cr, uid, ids, context=context)
        
        npp_obj = self.pool.get('sagi.new_product_project')
        
        if not isinstance(ids, list):
            ids = [ids]
        for prj in self.browse(cr, uid, ids, context=context):
            npp_ids = npp_obj.search(cr, uid, [('project','=',prj.id)], context=context)
            if not isinstance(npp_ids, list):
                npp_ids = [npp_ids]
            npp_obj.compute_control_status(cr, uid, npp_ids, context=context)
        return ret

project()

