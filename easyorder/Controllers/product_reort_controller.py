from odoo import http
from odoo.http import request

class ProductCustomController(http.Controller):

    @http.route('/create/custom_product', type='json', auth='public', methods=['POST'], csrf=False)
    def create_custom_product(self, **kwargs):
        # Extract data from the POST request body
        product_data = kwargs

        # Check if necessary fields are present (you can add more validation as needed)
        if 'name' not in product_data or 'id' not in product_data:
            return {'error': 'Missing required fields'}

        # Create a new record in the 'product.custom' model
        product = request.env['product.custom'].create({
            'id': product_data.get('id'),
            'name': product_data.get('name'),
            'list_price': product_data.get('list_price', 0.0),
            'standard_price': product_data.get('standard_price', 0.0),
            'quantity': product_data.get('quantity', 0),
            'on_hand_qty': product_data.get('onHandQty', 0),
            'default_code': product_data.get('default_code', ''),
            'image_128': product_data.get('image_128', ''),
        })

        # Return a success response
        return {'status': 'success', 'product_id': product.id}
