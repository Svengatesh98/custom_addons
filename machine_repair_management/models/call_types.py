from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class CallTypes(models.Model):
    
    _name = "call.types"
    
    _description = "Call Types"
    
    _rec_name = "complete_name"


    name = fields.Char(string="Name",required = True)
    
    code = fields.Char(string="Code", required = True)
    
    complete_name = fields.Char(string="Complete Name", compute = "_compute_name")
    
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id,required=True)

    
    @api.depends('name','code')
    def _compute_name(self):
        for rec in self:
            if rec.code and rec.name:
                rec.complete_name = '[%s] %s' % (rec.code,rec.name )
            else:
                rec.complete_name = rec.name
                
                
    @api.constrains('code')
    def _check_valid_code(self):
        for rec in self:
            code_search = self.env['call.types'].search([('code','=',rec.code)])
            if len(code_search) > 1:
                raise ValidationError("Code is Unique one.Please give the unique Code")             
                
                
class MachineRepairSupport(models.Model):
    _inherit = 'machine.repair.support'
    
    
    @api.model
    def _default_call_type_id(self):
        call_type_search = self.env['call.types'].search([('name','=','Call Center')],limit=1)
        return call_type_search.id if call_type_search else False
    

    # call_types_id = fields.Many2one('call.types',string="Call Type")

    call_types_id = fields.Many2one('call.types',string="Call Type",default = _default_call_type_id)
    maintenance_type = fields.Selection([('corrective', 'Corrective'), ('preventive', 'Preventive')], string='Job Type', default="corrective")
    work_location_id = fields.Many2one('work.center.location',string = "Location - Work Center")
    # work_location_id = fields.Many2one('mrp.workcenter',string = "Location - Work Center")

    
    
    call_request_appointment_date = fields.Datetime(
        string='Requested Appointment Date & Time',
        default=fields.Datetime.now,
        copy=False,
    )
    
    technician_appointment_date = fields.Datetime(
        string='Appointment DateTime',
        default=fields.Datetime.now,
        copy=False,
    )
    
    call_center_comments = fields.Text(string="Call Center comments")
    
    location_id = fields.Many2one('hr.work.location',string = "Location")
    
    phone_number_bool = fields.Boolean(string="Phone number Bool" , default = False, compute = "_compute_phone_number_bool")
    
    
    @api.depends('phone')
    def _compute_phone_number_bool(self):
        for rec in self:
            rec.phone_number_bool = False
            if rec.phone:
                rec.phone_number_bool = True
                if rec.phone_number_bool:
                    partner_search = self.env['res.partner'].search([('mobile','=',rec.phone)],limit=1)
                    if partner_search:
                        rec.partner_id = partner_search
                        # rec.phone = partner_search.mobile
                        # if rec.partner_id:
                        #     rec.onchange_partner_id()
                        
                
    

    
    @api.onchange('location_id')
    def _onchange_location_id(self):
        for rec in self:
            if rec.location_id:
                location_lst = self.env['work.center.location'].search([
                    ('location_id', '=', rec.location_id.id)
                ]).ids
                return {'domain': {'work_location_id': [('id', 'in', location_lst)] if location_lst else [('id', '=', 0)]}}
            else:
                return {'domain': {'work_location_id': [('id', '=', 0)]}}
        
    





                
    
    


        
    
    