from odoo import models,fields,api
from odoo.exceptions import ValidationError



class tag(models.Model):
    _name='tag'
    
    name=fields.Char(required=1)
   