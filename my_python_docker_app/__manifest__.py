# __manifest__.py
{
    'name': 'My Python Docker App',
    'version': '1.0',
    'summary': 'A Python Docker app example for Odoo Marketplace.',
    'author': 'JS',
    'maintainer': 'Navan',
    'website': 'https://nchat.navan.ai',
    'category': 'Custom',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'views/my_docker_model_views.xml',
        'views/templates.xml',
    ],
    'images': ['static/description/cover.png'],  # Added line for cover image
    'installable': True,
    'application': True,
}
