# -*- coding: utf-8 -*-
{
    'name': 'POS Learning',
    'version': '17.0.1.0.0',
    'category': 'Point of Sale',
    'summary': """Pos Learning """,
    'description': """Pos Learning First Module""",
    'author': 'Arunagiri',
    'company': 'Cielo Digital Solutions',
    'maintainer': 'Cielo Digital Solutions',
    'website': "http://www.cielo.com",
    'depends': ['point_of_sale','base'],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_session_view.xml'
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_learning/static/src/js/pos_store.js',
            'pos_learning/static/src/js/custom_button.js',
            'pos_learning/static/src/js/custom_popup.js',
            'pos_learning/static/src/js/pos_combos_button.js',
            'pos_learning/static/src/js/pos_combos_screen.js',
            'pos_learning/static/src/js/pos_custom_button.js',
            'pos_learning/static/src/js/pos_learning_records.js',
            'pos_learning/static/src/js/pos_learning_popup.js',
            'pos_learning/static/src/js/pos_receipt.js',
            # 'pos_learning/static/src/js/custom_barcode.js',
            'pos_learning/static/src/views/custom_popup.xml',
            'pos_learning/static/src/views/custom_button.xml',
            'pos_learning/static/src/views/pos_combo_button.xml',
            'pos_learning/static/src/views/pos_combo_screen.xml',
            'pos_learning/static/src/views/pos_custom_button.xml',
            'pos_learning/static/src/views/pos_learning_screen.xml',
            'pos_learning/static/src/views/pos_learning_popup.xml',
            'pos_learning/static/src/views/order_receipt.xml'

        ],
    },
   # 'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
