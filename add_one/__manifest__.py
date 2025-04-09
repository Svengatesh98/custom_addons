{
    'name': 'Add one',
    'version': '1.0',
    'summary': 'A simple todo list app using OWL in Odoo',
    'description': 'Manage your tasks with this OWL-based todo list application.',
    'author': 'Your Name',
    'category': 'Productivity',
    'license': 'LGPL-3',
    'depends': ['base', 'web','mail','sale','account','stock','purchase'],
     # ✅ Added missing comma
     'data':[
       'security/ir.model.access.csv',
       'views/base_menu.xml',
       'views/property_view.xml',
       'views/owner_view.xml',
       'views/tag_view.xml',
       'views/sale_order_view.xml',
       "views/purchase_order.xml",
       "reports/sale_oreder.xml"
     ],
     'assets':{ 
       'web.assets_backend':[
         'add_one/static/src/css/property.css',
       ]},
      
     
    'installable': True,
    'application': True,
    'auto_install': False,
}
