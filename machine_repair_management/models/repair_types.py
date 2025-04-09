# -*- coding: utf-8 -*

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Repairtype(models.Model):
    _name = 'repair.type'
    _description = "Repair Type"
    
    name = fields.Char(
        string="Name",
        required=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    service_id = fields.Many2one(
        'service.nature',
        string="Service", required=True,
    )

    @api.constrains('code')
    def dupl_code(self):
      
        exiting_code = self.env['repair.type'].search([('code', '=', self.code)])
        if len(exiting_code)>1:
            raise ValidationError('Already Code %s is existing' % self.code)

