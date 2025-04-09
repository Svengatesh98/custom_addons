{
    'name': 'Pos Customziation',
    'version': '1.0',
    'summary': 'Button adding in Sales Module',
    'description': 'Manage your tasks with this OWL-based todo list application.',
    'author': 'Vengateshwaran.S',
    'category': 'Pos Customization',
    'license': 'LGPL-3',
    'depends': ['point_of_sale','base'],
    'data': [
        "security/ir.model.access.csv",
        "views/pos_learn_view.xml",
        
    ],
    'assets': {
           'point_of_sale._assets_pos':[
                 "pos_customization/static/src/js/pos_store.js",
                 "pos_customization/static/src/js/pos_createbutton.js",
                 "pos_customization/static/src/js/popup.js",
                 "pos_customization/static/src/js/quantity.js",
                 "pos_customization/static/src/xml/total_quantity.xml",
                 "pos_customization/static/src/xml/popup.xml",
                 "pos_customization/static/src/xml/popupbutton.xml",
                 "pos_customization/static/src/xml/payment_screen.xml", 
                 "pos_customization/static/src/js/patch_product_card.js",
                 "pos_customization/static/src/xml/pos_screen.xml",
    ]
    },

    'installable': True,
    'application': True,
    'auto_install': False,
}
