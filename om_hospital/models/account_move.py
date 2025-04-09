from odoo import api,models,fields,_



class accountmove(models.Model):
    _inherit='account.move'
    
    appointment_id=fields.Many2one('hospital.appointment',string='Appoinment')
    