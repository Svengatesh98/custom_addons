
# models/custom_model.py
from odoo import models, fields

class CustomModel(models.Model):
    _name = 'custom.model'
    name = fields.Char('Name')
    description = fields.Text('Description')
