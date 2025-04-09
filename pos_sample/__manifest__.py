# __manifest__.py
{
    'name': 'POS Sample Module',
    'version': '1.0',
    'summary': 'A sample module for Odoo 17 POS',
    'description': 'This module adds a custom button to the POS interface.',
    'author': 'Your Name',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_order_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_sample/static/src/js/pos_sample.js',
            'pos_sample/static/src/xml/pos_sample.xml',
        ],
    },
    'installable': True,
    'application': True,
}