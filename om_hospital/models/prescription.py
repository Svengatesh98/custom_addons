from odoo import fields, models,api

class HospitalPrescription(models.Model):
    _name = 'hospital.prescription'
    _description = 'Prescription'
    
       
    name = fields.Char(string='Prescription Number',  copy=False, readonly=True)
    # name = fields.Char(string='Prescription Number', required=True, default='')
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    medication = fields.Char(string='Medication', required=True)
    dosage = fields.Char(string='Dosage', required=True)
    instructions = fields.Char(string='Instructions')
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection([
        ("draft", "Draft"),
        ("confirmed", "Confirmed"),
        ("ongoing", "Ongoing"),
        ("done", "Done"),
        ("cancel", "Canceled")
    ], string='Status', default="draft")
    name_tooltip = fields.Char(compute="_compute_name_tooltip", store=False)
    medicine_line_ids=fields.One2many('medicine',"prescription_id",string="Dosage")

    

    # @api.model
    # def create(self, vals):
    #     if vals.get('name', 'New') == 'New':
    #         vals['name'] = self.env['ir.sequence'].next_by_code('hospital.prescription') or '/'
    #     return super(HospitalPrescription, self).create(vals)
    @api.depends('patient_id', 'doctor_id')
    def _compute_name_tooltip(self):
        for record in self:
            doctor_name = record.doctor_id.name if record.doctor_id else "Unknown Doctor"
            patient_name = record.patient_id.name if record.patient_id else "Unknown Patient"
            record.name_tooltip = f"Doctor: {doctor_name}, Patient: {patient_name}"

    @api.model
    def create(self, vals):
        # Get sequence number
        sequence_number = self.env['ir.sequence'].next_by_code('hospital.prescription') or '/'

        # Get patient and doctor names
        patient = self.env['hospital.patient'].browse(vals.get('patient_id'))
        doctor = self.env['hospital.doctor'].browse(vals.get('doctor_id'))
        patient_id = patient.id if patient else 'Unknown'
        doctor_id = doctor.id if doctor else 'Unknown'
        # Generate unique Prescription Number
        vals['name'] = f"PPID/{doctor_id}/{patient_id}/{sequence_number}"

        return super(HospitalPrescription, self).create(vals)
                     
    # @api.model
    # def create(self, vals):
    #     if vals.get('name', 'New') == 'New':
    #         # Generate a new prescription number using sequence
    #         vals['name'] = self.env['ir.sequence'].next_by_code('hospital.prescription') or 'New'
    #     return super(HospitalPrescription, self).create(vals)
    
    def action_confirm(self):
        for rec in self:
            rec.state ='confirmed'
     
         
    def action_confirm(self):
        for rec in self:
            print("Button Is Clicked")

    def action_confirm(self):
        for rec in self:
            print("Button Is Clicked")

    def action_confirm(self):
        for rec in self:
            print("Button Is Clicked")
    def action_confirm(self):
        for rec in self:
            print("Button Is Clicked")
