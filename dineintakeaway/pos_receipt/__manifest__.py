{
    'name': "PoS receipt header",
    'version': '17.0.1.0.2',
    'category': 'Point of Sale',
    'summary': '',
    'description': "",
    'author': "Vengateshwaran.S",
    'company': 'Cielo Digital Solutions',
    'depends': ['point_of_sale','base','cd_dinetakeaway'],
    'data': [
       
    ],
    'assets': {
        'point_of_sale._assets_pos': [
           "pos_receipt/static/src/xml/pos_screen.xml",
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}