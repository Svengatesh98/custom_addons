from odoo import fields, models,api,_
from odoo.exceptions import UserError,ValidationError
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit=['mail.thread']
    _description = 'Patient Master'

    name = fields.Char(string="Name", required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    # doctor = fields.Char(string="DoctorName", required=True)
    age=fields.Integer(string="Age", compute="_compute_age", store=True)
    gender=fields.Selection(
        [
        ('male','Male'),
        ('female','Female')
        ])
    doctor_id = fields.Many2one("hospital.doctor", string="Doctor")
    patient_type = fields.Selection([
        ('child', 'Child'),
        ('adult', 'Adult'),
        ('senior', 'Senior Citizen'),
        ('elderly', 'Elderly (80+)'),
    ], string="Patient Type", compute="_compute_patient_type", store=True)
    patient_image = fields.Binary(string="Patient Image" ,attachment=True)
    is_minor=fields.Boolean(string="Minor")
    guardian=fields.Char(string="Guardian")



    @api.constrains("date_of_birth")
    def _check_birth_date(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth == date.today():
                raise ValidationError("Date of birth cannot be today")
  
  
    @api.depends("date_of_birth")
    def _compute_age(self):
        today = date.today()
        
        for rec in self:
            if rec.date_of_birth:
                rec.age=today.year -rec.date_of_birth.year - ((today.month,today.day)<(rec.date_of_birth.month,rec.date_of_birth.day))
            else:
                rec.age=0
            
            
    @api.ondelete(at_uninstall=False)  
    def _check_patient_appoinments(self):
        for record in self:
            domain=[('patient_ids','=',record.id)]
            appoinments=self.env['hospital.appointment'].search(domain)
            if appoinments:
                raise UserError(_("you cannot delete the patients now.""\nAppoinments existing for this patient :%s " %record.name))
           
                    
    # def unlink(self):
    #     for record in self:
    #         domain=[('patient_ids','=',record.id)]
    #         appoinments=self.env['hospital.appointment'].search(domain)
    #         if appoinments:
    #             raise UserError(_("you cannot delete the patients now.""\nAppoinments existing for this patient :%s " %record.name))
    #         return super().unlink()
            
        
        
    @api.depends('age')
    def _compute_patient_type(self):
        """Classify patients as 'Child', 'Adult','Senior',or,'Elderly'"""
        for record in self:
            record.patient_type='child' if record.age < 18 else 'elderly' if record.age >=80 else 'senior' if record.age >=60 else 'adult'
            # if record.age < 18:
            #     record.patient_type = 'child'
            # elif record.age >=80:
            #     record.patient_type = 'elderly'
            # elif record.age >= 60:
            #     record.patient_type = 'senior'
            # else:
            #     record.patient_type = 'adult'
                
                # @api.depends('age')
# def _compute_patient_type(self):
#     for record in self:
#         print(f"Computing for {record.name}, Age: {record.age}")  # Debug
#         record.patient_type = 'child' if record.age < 18 else 'elderly' if record.age >= 80 else 'senior' if record.age >= 60 else 'adult'
#         print(f"Assigned: {record.patient_type}")  # Debug

        