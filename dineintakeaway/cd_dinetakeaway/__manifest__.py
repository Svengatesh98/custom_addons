{
    'name': "Pos Restaurant Dine In/Take Away",
    'summary': """ Pos Restaurant Dine In/Take Away.""",
    'description': """
        This Module add dine in /takeaway facility in point of sale.
    """,
    'author': 'Vengateshwaran.S',
    'company': 'Cielo Digital Solutions',
    'license':'OPL-1',	
    'category': 'Pos',
    'version': '17.0',
    'depends': ['point_of_sale','pos_restaurant','base'],
   
    'data': [
       "views/pos_order_view.xml",
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            "cd_dinetakeaway/static/src/js/dine_in_button.js",
            "cd_dinetakeaway/static/src/js/takeaway_button.js",
            "cd_dinetakeaway/static/src/xml/control_button.xml",
            "cd_dinetakeaway/static/src/js/model.js",   
        ],
    }   
}
