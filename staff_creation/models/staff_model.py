from odoo import models, fields, api, _

class CustomCompanyStaff(models.Model):
    _name = 'custom.company.staff'
    _description = 'Custom Company Staff'

    name = fields.Char(string='School Name', required=True)
    number = fields.Char(string='School Identification Number', required=True)
    sequence = fields.Integer(string='Sequence')
    company_id = fields.Many2one('res.company', string='Company', required=True)
    staff_line_ids = fields.One2many('custom.company.staff.line', 'staff_id', string='Staff Members')
    doj=fields.Date(string="Date Of Joining")
    
    
    
class CustomCompanyStaffLine(models.Model):
    _name = 'custom.company.staff.line'
    _description = 'Custom Company Staff Line'

    name = fields.Char(string='Staff Name', required=True)
    age = fields.Integer(string='Age')
    dob = fields.Date(string='Date of Birth')
    department = fields.Char(string='Department')
    staff_id = fields.Many2one('custom.company.staff', string='Company Staff', ondelete='cascade')
    doj=fields.Date(string="Date Of Joining", related='staff_id.doj')
    # date = fields.Date('date', compute='_date_compute')
    date = fields.Date('date')

    
    # @api.depends('staff_id.doj')
    # def _date_compute(self):
    #     for rec in self:
    #         if rec.staff_id.doj:
    #             rec.date = rec.staff_id.doj
    #             print("rec.date", rec.date)
    #         else:
    #             rec.date = False
    
    @api.onchange('staff_id.number')
    def _date_compute(self):
        for rec in self:
            rec.date = False
            if rec.staff_id.number:
                rec.date = rec.staff_id.doj
                print("rec.date", rec.date)
            # else:
            #     rec.date = False            
                
