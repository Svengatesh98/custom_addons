{
    'name': 'owl Button',
    'version': '1.0',
    'summary': 'Button adding in Sales Module',
    'description': 'Manage your tasks with this OWL-based todo list application.',
    'author': 'Vengateshwaran.S',
    'category': 'Productivity',
    'license': 'LGPL-3',
    'depends': ['base', 'web','sale_management'],
    'data': [
        "sale_customer.xml",
        
    ],
    'assets': {
        'web.assets_backend': [
            "owl_todo_list/static/src/js/todo_list_controller.js",
            "owl_todo_list/static/src/xml/owl_todolist_controller.xml",
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
}
