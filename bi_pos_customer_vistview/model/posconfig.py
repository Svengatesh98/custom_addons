from odoo import models, fields

class PosConfig(models.Model):
    _inherit = "pos.config"
    
    res_customer_id=fields.Many2many('res.partner',string="Customer")
