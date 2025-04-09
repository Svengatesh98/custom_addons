{
    'name': "POS Customer List view  ",
    'version': '17.0.0.0',
    'category': 'Point of Sale',
    'author': 'Vengateshwaram',
    'depends': ['base', 'point_of_sale'],
    'data': [

    ],
    'assets': {
        'point_of_sale._assets_pos': [
           "bi_pos_customer_vistview/static/src/js/model.js",
        ],
    },
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False,
}