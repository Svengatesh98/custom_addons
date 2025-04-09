from odoo import models, fields

class ProductCustom(models.Model):
    _name = 'product.custom'
    _description = 'Custom Product Table'

    # Define the fields based on the structure you provided
    id = fields.Integer('ID', required=True)
    name = fields.Char('Name', required=True)
    list_price = fields.Float('List Price')
    standard_price = fields.Float('Standard Price')
    quantity = fields.Integer('Quantity')
    on_hand_qty = fields.Integer('On Hand Quantity')
    default_code = fields.Char('Default Code', required=False)
    image_128 = fields.Image('Image 128', required=False)

    # You can add other methods here as needed
