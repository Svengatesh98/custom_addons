
from odoo import models, fields, api


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Master'



    SPECIALTY_SELECTION = [
    ('general', 'General Physician'),
    ('cardio', 'Cardiologist'),
    ('derma', 'Dermatologist'),
    ('neuro', 'Neurologist'),
    ('ortho', 'Orthopedic'),
    ('pediatric', 'Pediatrician'),
    ('radiology', 'Radiologist'),
]
    id=fields.Integer()
    name = fields.Char()
    # specialty = fields.Char(string="Specialty")
    specialty = fields.Selection(
        selection= SPECIALTY_SELECTION,
        string="Specialty", 
        required=True, 
        default='general')
  

    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    active = fields.Boolean(string="Active", default=True)
    patient_ids = fields.One2many("hospital.patient", "doctor_id",required=True, string="Patients")
    
    
