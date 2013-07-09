# -*- encoding: utf-8 -*-
########################################################################
#                                                                       
# Copyright (C) 2009  Domsense s.r.l.                                   
# @authors: Simone Orsi																	       
# Copyright (C) 2009-2013  Alistek Ltd                                  
#                                                                       
#This program is free software: you can redistribute it and/or modify   
#it under the terms of the GNU General Public License as published by   
#the Free Software Foundation, either version 3 of the License, or      
#(at your option) any later version.                                    
#
# This module is GPLv3 or newer and incompatible
# with OpenERP SA "AGPL + Private Use License"!
#                                                                       
#This program is distributed in the hope that it will be useful,        
#but WITHOUT ANY WARRANTY; without even the implied warranty of         
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
#GNU General Public License for more details.                           
#                                                                       
#You should have received a copy of the GNU General Public License      
#along with this program.  If not, see <http://www.gnu.org/licenses/>.  
########################################################################

{
    'name': 'Aeroo Reports Multicompany',
    'version': '1.1',
    'category': 'Generic Modules/Aeroo Reporting',
    'description': """
Extends Aeroo Report to suport Multicompany
""",
    'author': 'Sistemas ADHOC',
    'website': 'http://www.sistemasadhoc.com.ar',
    'complexity': "easy",
    'depends': ['report_aeroo'],
    "init_xml" : [],
    'update_xml': ["report_view.xml", "report_aeroo_security.xml"],
    "license" : "GPL-3 or any later version",
    'installable': True,
    'active': False,
    'application': True,
}
