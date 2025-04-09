from odoo import models, fields

class ProductProduct(models.Model):
    _inherit = 'product.product'

    extra_barcodes_ids = fields.One2many(
        'product.barcode',
        'product_id',
        string='Extra Barcodes'
    )


class ProductBarcode(models.Model):
    _name = 'product.barcode'
    _description = 'Extra Product Barcode'

    name = fields.Char('Barcode', required=True)
    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True,
        ondelete='cascade'
    )
