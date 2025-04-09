{
    'name': 'owl Learn',
    'version': '1.0',
    'summary': 'A simple todo list app using OWL in Odoo',
    'description': 'Manage your tasks with this OWL-based todo list application.',
    'author': 'Your Name',
    'category': 'Productivity',
    'license': 'LGPL-3',
    'depends': ['base', 'web',],
    'data': [
        'security/ir.model.access.csv',  # Ensure this file exists
        'views/owl_todolist_views.xml',  # Ensure this file exists
    ],
    'assets': {
        # # Assets for Point of Sale
        # 'point_of_sale.assets': [
        #     'owl_Learn/static/src/js/custom_pos_receipt.js',
        #     'owl_Learn/static/src/xml/pos_screen.xml',
        # ],
        # Assets for the backend (web interface)
        'web.assets_backend': [
            'owl_Learn/static/src/js/action_todo_list_js.js',
            'owl_Learn/static/src/xml/todo_list_template.xml',
   
            
        ],
    },
    # "assets": {
        
    # 'point_of_sale._assets_pos': [
    #     'custom_pos_receipt/static/src/js/custom_pos_receipt.js',
    #  ]

    #     "web.assets_backend": [
    #         "owl_Learn/static/src/js/action_todo_list_js.js",
    #         "owl_Learn/static/src/xml/todo_list_template.xml",
    #     ],
      
          
    # },  # ✅ Added missing comma

    'installable': True,
    'application': True,
    'auto_install': False,
}
