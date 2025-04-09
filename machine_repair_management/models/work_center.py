from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class WorkCenter(models.Model):
    
    _name = "work.center.location"
    
    _description = " Work Center Location"
    
    _rec_name = "complete_name"
    
    
    name = fields.Char(string='Name',required = True)
    code = fields.Char(string="Code", required = True)
    location_id = fields.Many2one('hr.work.location',string="Location")
    company_id = fields.Many2one('res.company', string = "Company" , default = lambda self:self.env.user.company_id)
    complete_name = fields.Char(string="Complete Name" , compute = "_compute_complete_name")
    
    
    @api.constrains('code')
    def _check_validity_code(self):
        for rec in self:
            code_search = self.env['work.center.location'].search([('code','=',rec.code)])
            if len(code_search) > 1:
                raise ValidationError('Code is unique one.Please enter code for the work location')
                
    @api.depends('name','code')
    def _compute_complete_name(self):
        for rec in self:
            if rec.name and rec.code:
                rec.complete_name = '[%s] %s' %(rec.code,rec.name)
            else:
                rec.complete_name = rec.name     
    
