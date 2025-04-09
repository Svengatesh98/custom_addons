from odoo import models, fields,api,_


class Product_service_type(models.Model):
    _inherit='product.category'
    
    def_servicetypeid=fields.Many2one('service.nature',string='Service Type')
    warranty_period = fields.Integer(string="Warranty Period", help="Default warranty period for the category.")
    warranty_period_combo = fields.Selection([
        ('days', 'Days'),
        ('months', 'Months'),
        ('years', 'Years'),
    ], string="Warranty Period Unit",default='months',help="Unit of the warranty period (Days, Months, Years).")
    
 