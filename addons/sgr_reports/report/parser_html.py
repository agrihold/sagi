##############################################################################
#
# Copyright (c) 2008-2011 Alistek Ltd (http://www.alistek.com) All Rights Reserved.
#                    General contacts <info@alistek.com>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This module is GPLv3 or newer and incompatible
# with OpenERP SA "AGPL + Private Use License"!
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from report import report_sxw
from report.report_sxw import rml_parse
from datetime import date
from openerp.report import report_sxw
from openerp.tools import float_compare
from openerp import netsvc

class Parser(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
        print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
        print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
        
        ret = super(Parser, self).__init__(cr, uid, name, context)
        
        print_id = context.get('print_id', False)
        aeroo_print = self.active_prints[print_id] # Aeroo print object
        aeroo_ooo = context.get('aeroo_ooo', False)
        
        localcontext['include_html'] = self._include_html(aeroo_print, print_id, aeroo_ooo)
        
        return ret

    def _include_html(self, aeroo_print, print_id, aeroo_ooo=False):
        def include_html(data):
            print '######################################################'
            print '######################################################'
            print '######################################################'
            print '######################################################'
            print 'data: ' + str(data)
            with NamedTemporaryFile(suffix='.odt', prefix='aeroo-report-', delete=False) as temp_file:
                    temp_file.write(data)
            #temp_file.close()
            print 'temp_file.name: ' + str(temp_file.name)
            print 'temp_file.close'
            self.active_prints[print_id].subreports.append(temp_file.name)
            aeroo_print.subreports.append(temp_file.name)
            return "<insert_doc('%s')>" % temp_file.name
        return include_html


