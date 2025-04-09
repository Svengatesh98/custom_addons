from odoo import models, fields

class SwipeRecord(models.Model):
    _name = "swipe.record"
    _description = "Swipe Action Records"

    name = fields.Char(string="Item Name", required=True)
    status = fields.Selection([
        ('starred', 'Starred'),
        ('deleted', 'Deleted'),
        ('default', 'Default')
    ], string="Status", default="default")
