{
    'name': "userflow",
    'summary': """Userflow connector""",
    'description': """Connector for import userflow.js""",
    'author': 'Sergii O.',
    'company': 'erpbox',
    'website': "https://www.erp-box.co",
    'category': 'Tools',
    'version': '16.0.0.6',
    'depends': [
        'base',
        'web',
        'website',
    ],
    'data': [],
    'installable': True,
    'application': False,
    'assets': {
        'web.assets_backend': [
            '/userflow/static/src/js/userflow_script.js',
	    'node_modules/userflow.js/dist/userflow.js',
        ],
    },
}
