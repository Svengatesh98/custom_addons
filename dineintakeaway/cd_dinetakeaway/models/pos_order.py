# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models,_

class PosOrder(models.Model):
    _inherit = 'pos.order'

    dine_in = fields.Boolean("Dine-in" , default = False)
    takeaway = fields.Boolean("Take away" , default = False)
    
    def _order_fields(self, create_from_ui):
        # res = super(PosOrder, self)._order_fields(create_from_ui) 
        res = super()._order_fields(create_from_ui)
        res['dine_in'] = create_from_ui.get('dine_in', False)
        res['takeaway'] = create_from_ui.get('takeaway', False)
        return res

    
    # def _order_fields(self, create_from_ui):
    #     res = super(PosOrder, self)._order_fields(create_from_ui)
    #     res['dine_in'] = create_from_ui['dine_in']
    #     res['takeaway'] = create_from_ui['takeaway']
    #     return res
    

# class PosSession(models.Model):
#     _inherit = 'pos.session'
    
#     def _loader_params_product_product(self):
#         """
#         Override to add custom product fields to POS loading
#         Returns:
#             dict: loader parameters for product.product
#         """
#         result = super()._loader_params_product_product()  # Fixed method name
#         result['search_params']['fields'].append("your_custom_field")
        
#         # Add more fields if needed
#         result['search_params']['fields'].extend([
#             'field1',
#             'field2',
#             # Add other custom fields here
#         ])
        
#         return result
          