from odoo import api,fields,models,_
from odoo.exceptions import ValidationError

class Defects(models.Model):
    _name='defects'
    _rec_name='def_servicetypeid'
    
    def_servicetypeid=fields.Many2one('service.nature',string='Service Type',required=True)
    def_code=fields.Char(string='Defect Code ',required=True)
    def_desc=fields.Char(string='Defect Description ',required=True)
    


    @api.constrains('def_servicetypeid', 'def_code')
    def _check_defectstype_valid_code(self):
        for rec in self:
            defects_search = self.env['defects'].search([('def_servicetypeid','=',rec.def_servicetypeid.id),('def_code','=',rec.def_code)])
            if len(defects_search) > 1:
                raise ValidationError("The combination of Service Type and Defect Code must be unique!")     




