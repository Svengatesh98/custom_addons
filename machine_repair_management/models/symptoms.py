from odoo import models, fields, api,_
from odoo.exceptions import ValidationError

class Symptoms(models.Model):
    _name='symptoms'
    _rec_name="sym_servicetypeid"

    sym_servicetypeid=fields.Many2one('service.nature',string='Service Type', required=True)
    sym_code=fields.Char(string='Symptoms Code',required=True )
    sym_desc=fields.Char( string='Symptoms Description' ,required=True, translate=True)
       
    @api.constrains("sym_servicetypeid", "sym_code")
    def _check_unique_servicetype_symptoms(self):
        for rec in self:
            domain = [
                ("sym_servicetypeid", "=", rec.sym_servicetypeid.id),
                ("sym_code", "=", rec.sym_code),
            ]
            existing = self.env['symptoms'].search(domain)
            if len(existing)>1:
                raise ValidationError("The combination of Service Type and Symptoms Code must be unique!")
               
    # @api.constrains("sym_servicetypeid", "sym_code")
    # def _check_valid_code(self):
    #     for rec in self:
    #         code_search = self.env['call.types'].search([('code','=',rec.code)])
    #         if len(code_search) > 1:
    #             raise ValidationError("Code is Unique one.Please give the unique Code")             
                