{
    'name': 'Easy Order',
    'version': '1.0',
    'summary': 'A simple todo list app using OWL in Odoo',
    'description': 'Manage your tasks with this OWL-based todo list application.',
    'author': 'Your Name',
    'category': 'Sale and Purchase',
    'license': 'LGPL-3',
    'depends': ['purchase', 'sale', 'sale_management','product', 'stock'],
    'data': [
        "security/ir.model.access.csv",
        'views/ir_actions_server.xml',
    #     "views/report_shoppint_cart.xml",
    ],
    'controllers':[
        "Controllers/product_reort_controller.py",
    ],
    'assets': {
        'web.assets_backend': [
            'easyorder/static/src/Components/main/base_component.js',
            'easyorder/static/src/Components/main/base_component.xml',
            "easyorder/static/src/Components/product/product_component.js",
            "easyorder/static/src/Components/product/product_component.xml",
            "easyorder/static/src/Components/cart/cart_component.js",
            "easyorder/static/src/Components/cart/cart_component.xml",
            # "easyorder/static/src/services/products_service.js"
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
