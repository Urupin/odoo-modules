# -*- coding: utf-8 -*-
{
    'name': "userflow",

    'summary': """Userflow connector""",

    'description': """Connector for import userflow.js """,

    'author': 'Sergii O.',
    'company': 'erpbox',
    'website': "https://www.erp-box.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '16.0.0.3',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'web',
        'website',
    ],
 
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
	'views/userflow_template.xml',
    ],
    'installable': True,
    'application': False,
}
