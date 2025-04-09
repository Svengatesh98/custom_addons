# __manifest__.py
{
    'name': 'Custom POS Module',
    'version': '1.0',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],  # POS module dependency
    'data': [
        'views/pos_assets.xml',  # XML file to include JS for POS
    ],
    'installable': True,
    'auto_install': False,
}
