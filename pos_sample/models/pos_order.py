# models/pos_order.py
from odoo import models, fields

class PosOrder(models.Model):
    _inherit = 'pos.order'

    custom_field = fields.Char(string='Custom Field')