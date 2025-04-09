
from odoo import models, fields,api
from odoo.exceptions import ValidationError

class Medicine(models.Model):
    _name = "medicine.management"
    _description = "Medicine Management"
    
    
    id=fields.Integer()
    name = fields.Char(string="Medicine Name", required=True)
    code=fields.Char(string='code', required=True)
    medicine_type = fields.Selection([
        ('tablet', 'Tablet'),
        ('capsule', 'Capsule'),
        ('syrup', 'Syrup'),
        ('injection', 'Injection'),
        ('ointment', 'Ointment'),
        ('drops', 'Drops'),
        ('other', 'Other')
        ], string='MedicineType', default='tablet')
    
    # purpose=fields.Selection([
    #     ('general_checkup', 'General Check-up'),
    #     ('chronic_disease', 'Chronic Disease Treatment'),
    #     ('infection', 'Infection Treatment'),
    #     ('pain_relief', 'Pain Relief'),
    #     ('removes phiegma', 'Removes Phlegma'),
    #     ('for fever', 'For Fever'),
    #     ('bacterial infection', 'Bacterial Infection'),
       
    #     ('mental_health', 'Mental Health Treatment'),
    #     ('other', 'Other')
    # ], string="Purpose", required=True, default='general_checkup')
    # dosagevalue=fields.Char(string="Dosage")
    # route=fields.Char(string="Route")
    # duration=fields.Char(string="Duration")
    
    # @api.onchange('name')
    # def _onchange_medicine(self):
        # """Auto-fill dosage, route, and duration when selecting a medicine"""
        # if self.name:
        #     self.purpose=self.name.purose
        #     self.dosagevalue = self.name.dosagevalue
        #     self.route = self.name.route
        #     self.duration = self.name.duration
    