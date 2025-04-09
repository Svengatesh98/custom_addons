from odoo import api, fields,models

class PatientTag(models.Model):
    _name='patient.tag'
    _description='patient_master'
    
    name=fields.Char(string='Name',required=True ,tracking=True)
    # date_of_birth=fields.Date(string='Dob',tracking=True)
    # gender=fields.Selector(
    #     [
    #     ('male','Male'),
    #     ('female','Female')
    #     ],string='Gender' ,tracking=
    
    