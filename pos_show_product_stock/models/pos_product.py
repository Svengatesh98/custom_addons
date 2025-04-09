
from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def _pos_ui_model_product_product(self):
        result = super()._pos_ui_model_product_product()
        for product in result:
            product['qty_available'] = self.browse(product['id']).qty_available
        return result
