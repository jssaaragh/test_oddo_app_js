# __manifest__.py
{
    'name': 'My Python Docker App',
    'version': '1.0',
    'summary': 'A Python Docker app example for Odoo Marketplace.',
    'author': 'Your Name',
    'maintainer': 'Your Name/Company',
    'website': 'https://www.yourwebsite.com',
    'category': 'Custom',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'views/my_docker_model_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
}