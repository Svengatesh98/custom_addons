from odoo import api, models, fields, _


class HospitalAppoinment(models.Model):
    _name = 'hospital.appointment'
    # _inherit = ['mail.thread.main.attachment', 'mail.activity.mixin']
    _inherit = ['mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _rec_name = 'patient_ids'
    reference = fields.Char(string="Reference", 
                            readonly=True,)
    patient_ids = fields.Many2one(
        'hospital.patient', string='patient', ondelete='restrict')
    date_appointment = fields.Date(String='Date')
    note = fields.Text(string='note')


# @api.model
# def create(self, vals_list):
#     # Iterate through each dictionary in the list of values
#     for vals in vals_list:
#         print('Before:', vals)
#         # Generate reference only if it's missing or 'New'
#         if not vals.get('reference') or vals['reference'] == 'New':
#             vals['reference'] = self.env['ir.sequence'].next_by_code(
#                 'hospital.appointment')
#         print('After:', vals)
#         return super().create(vals_list)

# @api.model
# def create(self, vals_list):
    # Ensure vals_list is a list (Odoo sometimes passes a single dict)
    # if isinstance(vals_list, dict):
    #     vals_list = [vals_list]

    # for vals in vals_list:
    #     print('Before:', vals)
    #     # Generate reference only if missing or set to 'New'
    #     if not vals.get('reference') or vals['reference'] == 'New':
    # sequence_number = self.env['ir.sequence'].next_by_code('hospital.prescription') or '/'

    #     # Get patient and doctor names
    #     patient = self.env['hospital.patient'].browse(vals.get('patient_id'))
    #     doctor = self.env['hospital.doctor'].browse(vals.get('doctor_id'))
    #     patient_id = patient.id if patient else 'Unknown'
    #     doctor_id = doctor.id if doctor else 'Unknown'
    #     # Generate unique Prescription Number
    #     vals['name'] = f"PPID/{doctor_id}/{patient_id}/{sequence_number}"

    #     return super(HospitalPrescription, self).create(vals)
   
    # name = self.env['ir.sequence'].next_by_code('hospital.appointment') or '/'
    # print("/////////name",name)
    # vals_list['reference']=name
    # print('After:', vals_list)

    # return super(HospitalAppoinment,self).create(vals_list)

# @api.model
# def create(self, vals):
#     if vals.get('reference', 'New') == 'New':
#         vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.prescription') or '/'
#     return super(HospitalAppoinment, self).create(vals)

@api.model
def create(self, vals):
    # Ensure that the reference is set when creating a record
    if not vals.get('reference'):
        # Print the values being passed to ensure correctness
        print("Creating Appointment with values: ", vals)
        vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or '/'
    
    # Call the super method to create the record
    return super(HospitalAppoinment, self).create(vals)
