{
    'name': 'Custom CRM Logo',
    'version': '1.0.0',
    'summary': 'Adds a custom logo to the CRM module.',
    'description': 'This module adds a custom logo to the CRM interface.',
    'author': 'SWIT',
    'category': 'Customization',
    'depends': ['web'],
    'data': ['views/assets.xml'],
    'assets': {
        'web.assets_backend': [
            '/custom_crm_logo/static/img/my_logo.png',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
