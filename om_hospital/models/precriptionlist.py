from odoo import models,fields,api,_
 
class Medicine(models.Model):
    
    _name='medicine'
    _description=""
    
    prescription_id=fields.Many2one("hospital.prescription")
    name=fields.Many2one("medicine.management")
    purpose=fields.Selection([
        ('general_checkup', 'General Check-up'),
        ('chronic_disease', 'Chronic Disease Treatment'),
        ('infection', 'Infection Treatment'),
        ('pain_relief', 'Pain Relief'),
        ('removes phiegma', 'Removes Phlegma'),
        ('for fever', 'For Fever'),
        ('bacterial infection', 'Bacterial Infection'),
       
        ('mental_health', 'Mental Health Treatment'),
        ('other', 'Other')
    ], string="Purpose", required=True, default='general_checkup')
    dosagevalue=fields.Char(string="Dosage")
    route=fields.Char(string="Route")
    duration=fields.Char(string="Duration")
    # name=fields.Char(string="MedicineName")
    # numbers=fields.Integer(string="No of tablets")
    # before_breakfast=fields.Integer(string="Before breakfast Quantity")
    # after_breakfast=fields.Integer(string="Before breakfast Quantity")
    # before_lunch=fields.Integer(string="Before lunch Quantity")
    # after_lunch=fields.Integer(string="Before lunch Quantity")
    # before_dinner=fields.Integer(string="Before dinner Quantity")
    # after_dinner=fields.Integer(string="After dinner Quantity")
    
   

    
    
    