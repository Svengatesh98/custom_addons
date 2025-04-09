from odoo import models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def _loader_params_product_product(self):
        res = super()._loader_params_product_product()
        res["fields"].append("qty_available")
        return res
