# -*- coding: utf-8 -*-

import time
from odoo.exceptions import UserError
from odoo import models, fields, api, _
from odoo.exceptions import UserError, warnings, ValidationError
from datetime import datetime

class MachineRepairSupport(models.Model):
    _name = 'machine.repair.support'
    _description = 'Machine Repair Support'
    _order = 'id desc'
#     _inherit = ['mail.thread', 'ir.needaction_mixin']
    _inherit = ['mail.thread', 'mail.activity.mixin', 'format.address.mixin','portal.mixin']

    
    @api.model
    def create(self, vals):

        if vals.get('custome_client_user_id', False):
            client_user_id = self.env['res.users'].browse(int(vals.get('custome_client_user_id')))
            if client_user_id:
                vals.update({'company_id': client_user_id.company_id.id})
        else:
            vals.update({'custome_client_user_id': self.env.user.id})


        if vals.get('name', False):
            if not vals.get('name', 'New') == 'New':
                vals['subject'] = vals['name']
                
        if vals.get('name', 'New') == 'New':
            # vals['name'] = self.env['ir.sequence'].next_by_code('machine.repair.support') or 'New'
            location=vals.get('location_id', False)
            location_name= self.env['hr.work.location'].browse(location)
            print("Location:",location_name.name)
    
            loc_name=location_name.name[:3].upper() if location_name else 'NA'
            print("Location:",loc_name)
            current_date = datetime.today()
            current_year = datetime.today().strftime('%y') 
            current_month = datetime.today().strftime('%m')
            # loc_no=self.env['machine.repair.support'].search_count([('location_id','=',location_name.id)])
            loc_no=self.env['machine.repair.support'].search([('location_id','=',location_name.id)],limit=1)
            print(loc_no)
            #  OFF25040001
            formatted_num=""
            last_sequence = "0000" 
            last_month = None
            if loc_no:
                last_name = loc_no.display_name  
                last_month = last_name[5:7]  
                last_sequence = last_name[-4:] 
        
            if last_sequence.isdigit():
                if last_month == current_month:
                    new_loc_num = int(last_sequence) + 1
                    formatted_num = f"{new_loc_num:04d}"
                else:
                    formatted_num = "0001"
            # if loc_no:
            #     if loc_no.display_name[-4:].isdigit():
            #         new_loc_num = int(loc_no.display_name[-4:]) + 1
            #         formatted_num = f"{new_loc_num:04d}"
            #         print("Next loc number:", formatted_num)
            #     else:
            #         formatted_num = "0001"  
            #         print("Starting at:", formatted_num)
            # else:
            #     formatted_num = "0001"  
     

            # print(new_loc_num)
            
            vals['name']=f'{loc_name}{current_year}{current_month}{str(formatted_num).zfill(4)}'
            print("name:",vals['name'])
        
        
        
        if vals.get('partner_id', False):
            if 'phone' and 'email' not in vals:
                partner = self.env['res.partner'].sudo().browse(vals['partner_id'])
                if partner:
                    vals.update({
                        'email': partner.email,
                        'phone': partner.phone,
                    })

        """Create a lot if it does not exist when saving a repair order."""
        if 'product_id' in vals and 'product_slno' in vals:
            product = vals.get('product_id')
            lot_name = vals.get('product_slno')
            existing_lot = self.env['stock.lot'].search([
                ('name', '=', lot_name),('product_id', '=', product)], limit=1)

            if not existing_lot:
                new_lot = self.env['stock.lot'].create({
                    'name': lot_name,
                    'product_id': product,
                    'company_id': self.env.company.id
                })
        return super(MachineRepairSupport, self).create(vals)
    
#    @api.multi odoo13
    @api.depends('timesheet_line_ids.unit_amount')
    def _compute_total_spend_hours(self):
        for rec in self:
            spend_hours = 0.0
            for line in rec.timesheet_line_ids:
                spend_hours += line.unit_amount
            rec.total_spend_hours = spend_hours
    
    @api.onchange('project_id')
    def onchnage_project(self):
        for rec in self:
            rec.analytic_account_id = rec.project_id.analytic_account_id
          
#    @api.one odoo13
    def set_to_close(self, force_send=False):
        if self.is_close != True:
            self.is_close = True
            self.close_date = fields.Datetime.now()#time.strftime('%Y-%m-%d')
            self.state = 'closed'
            template = self.env.ref('machine_repair_management.email_template_machine_ticket', raise_if_not_found=False)
            # template.send_mail(self.id, force_send=force_send)
            
#    @api.one odoo13
    def set_to_reopen(self):
        self.state = 'work_in_progress'
        if self.is_close != False:
            self.is_close = False

#    @api.multi odoo13
    def create_machine_diagnosys(self):
        for rec in self:
            name = ''
            if rec.subject:
                name = rec.subject +'('+rec.name+')'
            else:
                name = rec.name
            task_vals = {
                'name' : str(name),
                # 'user_id' : rec.user_id.id,
                # 'activity_user_id': rec.user_id.id,
                'user_ids': [rec.user_id.id or self.env.user.id],
                # 'user_ids' : [(4, rec.user_id.id)],
                'date_deadline' : rec.close_date,
                'project_id' : rec.project_id.id,
                'partner_id' : rec.partner_id.id,
                'description' : rec.description,
                'machine_ticket_id' : rec.id,
                'task_type': 'diagnosys',
            }
            task_id= self.env['project.task'].sudo().create(task_vals)
        action = self.env.ref('machine_repair_management.action_view_task_diagnosis')
        result = action.sudo().read()[0]
        result['domain'] = [('id', '=', task_id.id)]
        return result

#    @api.multi odoo13
    def create_work_order(self):
        for rec in self:
            work_order_name = ''
            if rec.subject:
                work_order_name = rec.subject +'('+rec.name+')'
            else:
                work_order_name = rec.name
            task_vals = {
#            'name' : rec.subject +'('+rec.name+')', odoo13
            'name' : work_order_name,
            # 'user_id' : rec.user_id.id,
            # 'activity_user_id': rec.user_id.id,
            'user_ids': [rec.user_id.id or self.env.user.id],
            # 'user_ids' : [(4, rec.user_id.id)],
            'date_deadline' : rec.close_date,
            'project_id' : rec.project_id.id,
            'partner_id' : rec.partner_id.id,
            'description' : rec.description,
            'machine_ticket_id' : rec.id,
            'task_type': 'work_order',
            }
            task_id= self.env['project.task'].sudo().create(task_vals)
        action = self.env.ref('machine_repair_management.action_view_task_workorder')
        result = action.sudo().read()[0]
        result['domain'] = [('id', '=', task_id.id)]
        return result

    @api.onchange('product_id')
    def onchnage_product(self):
        for rec in self:
            rec.brand = rec.product_id.brand
            # rec.color = rec.product_id.color odoo13
            rec.color = rec.product_id.color_custom
            rec.model = rec.product_id.model
            rec.year = rec.product_id.year
    
    name = fields.Char(
        string='Number', 
        required=False,
        default='New',
        copy=False, 
        readonly=True, 
    )
    state = fields.Selection(
        [('new','New'),
         ('assigned','Assigned'),
         ('work_in_progress','Work in Progress'),
         ('needs_more_info','Needs More Info'),
         ('needs_reply','Needs Reply'),
         ('reopened','Reopened'),
         ('solution_suggested','Solution Suggested'),
         ('closed','Closed')],
        tracking=True,
        default='new',
        copy=False, 
    )
    email = fields.Char(
        string="Email",
        required=False
    )
    phone = fields.Char(
        string="Phone"
    )
    category = fields.Selection(
        [('technical', 'Technical'),
        ('functional', 'Functional'),
        ('support', 'Support')],
        string='Category',
    )
    subject = fields.Char(
        string="Subject"
    )
    description = fields.Text(
        string="Description"
    )
    priority = fields.Selection(
        [('0', 'Low'),
        ('1', 'Middle'),
        ('2', 'High')],
        string='Priority',
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
    )
    request_date = fields.Datetime(
        string='Create Date',
        default=fields.Datetime.now,
        copy=False,
    )
    close_date = fields.Datetime(
        string='Close Date',
    )
    user_id = fields.Many2one(
        'res.users',
        string='Technician',
    )
    department_id = fields.Many2one(
        'hr.department',
        string='Department'
    )
    timesheet_line_ids = fields.One2many(
        'account.analytic.line',
        'repair_request_id',
        string='Timesheets',
    )
    is_close = fields.Boolean(
        string='Is Ticket Closed ?',
        tracking=True,
        default=False,
        copy=False,
    )
    total_spend_hours = fields.Float(
        string='Total Hours Spent',
        compute='_compute_total_spend_hours'
    )
    project_id = fields.Many2one(
        'project.project',
        string='Project',
    )
    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string='Analytic Account',
    )
    team_id = fields.Many2one(
        'machine.support.team',
        string='Machine Repair Team',
        default=lambda self: self.env['machine.support.team'].sudo()._get_default_team_id(user_id=self.env.uid),
    )
    team_leader_id = fields.Many2one(
        'res.users',
        string='Team Leader',
    )
    journal_id = fields.Many2one(
        'account.journal',
         string='Journal',
     )
    task_id = fields.Many2one(
        'project.task',
        string='Task',
        readonly = True,
    )
    is_task_created = fields.Boolean(
        string='Is Task Created ?',
        default=False,
    )
    company_id = fields.Many2one(
        'res.company', 
        default=lambda self: self.env.user.company_id, 
        string='Company',
        readonly=False,
#        readonly=True,
     )
    comment = fields.Text(
        string='Customer Comment',
        readonly=True,
    )
    rating = fields.Selection(
        [('poor', 'Poor'),
        ('average', 'Average'),
        ('good', 'Good'),
        ('very good', 'Very Good'),
        ('excellent', 'Excellent')],
        string='Customer Rating',
        readonly=True,
    )
    product_category = fields.Many2one(
        'product.category',
        string="Product Category"
    )
    product_id = fields.Many2one(
        'product.product',
        domain="[('is_machine', '=', True)]",
        string="Product"
    )
    brand = fields.Char(
        string = "Brand"
    )
    color = fields.Char(
        string = "Color"
    )
    model = fields.Char(
        string="Model"
    )
    year = fields.Char(
        string="Year"
    )
    accompanying_items = fields.Text(
        string="Accompanying Items",
    )
    damage = fields.Text(
        string="Damage",
    )
    warranty = fields.Boolean(
        string="Warranty",
    )
    img1 = fields.Binary(
        string="Images1",
    )
    img2 = fields.Binary(
        string="Images2",
    )
    img3 = fields.Binary(
        string="Images3",
    )
    img4 = fields.Binary(
        string="Images4",
    )
    img5 = fields.Binary(
        string="Images5",
    )
    repair_types_ids = fields.Many2many(
        'repair.type',
        string="Repair Type"
    )
    problem = fields.Text(
       string="Problem",
    )
    cosume_part_ids = fields.One2many(
      'product.consume.part',
      'machine_id',
      string="ProduCt consume Part"
    )
    nature_of_service_id = fields.Many2one(
        'service.nature',
        string="Nature Of service"
    )
    lot_id = fields.Many2one(
        'stock.lot',
        string="Lot"
    )
    website_brand = fields.Char(
        string = "Website Brand"
    )
    website_model = fields.Char(
        string = "Website Model"
    )
    # website_year = fields.Char(
    #     string = "Website Year"
    # )
    website_year = fields.Datetime(
        string = "Website Year"
    )
#     @api.multi
#     @api.depends('analytic_account_id')
#     def compute_total_hours(self):
#         total_remaining_hours = 0.0
#         for rec in self:
#             rec.remaining_hours = rec.analytic_account_id.remaining_hours
#     
    total_consumed_hours = fields.Float(
        string='Total Consumed Hours',
#         compute='compute_total_hours',
#         store=True,
    )
    
    custome_client_user_id = fields.Many2one(
        'res.users',
        string="Ticket Created User",
        readonly = True,
        track_visibility='always'
    )
    product_slno = fields.Char(string="Serial Number")
    purchase_invoice_no = fields.Char(string="Purchase Invoice Number")
    purchase_date = fields.Date(string="Purchase Date")
    purchase_dealer_name = fields.Char(string="Dealer Name")
    
    

    @api.onchange('product_id')
    def onchange_product_serial_number(self):
        lot = self.env['stock.lot'].search([('product_id', '=', self.product_id.id)], order='create_date desc', limit=1)
        self.product_slno = lot.name

    # @api.constrains('product_id')
    # def product_slno_constrains(self):
    #     serial_no = self.env['stock.lot'].search([('product_id', '=', self.product_id.id)])
    #     if serial_no:
    #         raise ValidationError(('Already Lot/Serial Number has been created for the product %s' % self.product_id.name))



#    @api.multi odoo13
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for rec in self:
            if rec.partner_id:
                rec.email = rec.partner_id.email
                # rec.phone = rec.partner_id.phone

#    @api.multi odoo13
    @api.onchange('product_category')
    def product_id_change(self):
        return {'domain':{'product_id':[('is_machine', '=', True),('categ_id', '=', self.product_category.id)]}}

#    @api.multi odoo13
    @api.onchange('team_id')
    def team_id_change(self):
        for rec in self:
            rec.team_leader_id = rec.team_id.leader_id.id
    
#    @api.one odoo13
    def unlink(self):
        for rec in self:
            if rec.state != 'new':
                raise UserError(_('You can not delete record which are not in draft state.'))
        return super(MachineRepairSupport, self).unlink()
    
#    @api.multi odoo13
    def show_machine_diagnosys_task(self):
        for rec in self:
            res = self.env.ref('machine_repair_management.action_view_task_diagnosis')
            res = res.sudo().read()[0]
            res['domain'] = str([('task_type','=','diagnosys'), ('machine_ticket_id', '=', rec.id)])
            res['context'] = {'default_machine_ticket_id': rec.id, 'default_task_type': 'diagnosys'}
        return res
    
#    @api.multi odoo13
    def show_work_order_task(self):
        for rec in self:
            res = self.env.ref('project.action_view_task')
            res = res.sudo().read()[0]
            res['domain'] = str([('task_type','=','work_order'), ('machine_ticket_id', '=', rec.id)])
            res['context'] = {'default_machine_ticket_id': rec.id, 'default_task_type': 'work_order'}
        return res

    request_created_date = fields.Date(
        string='Call Date',
        compute='_compute_request_date_time',
    )

    request_created_time = fields.Char(
        string='Call Time',
        compute='_compute_request_date_time',
    )
    
    @api.depends('request_date')
    def _compute_request_date_time(self):
        for record in self:
            if record.request_date:
                record.request_created_date = record.request_date.date()
                record.request_created_time = record.request_date.strftime('%H:%M:%S')

    appt_created_date= fields.Char(
        string='Appt.Date',
        compute='_compute_appoint_date_time',
    )
    appt_created_time= fields.Char(
        string='Appt.Time',
        compute='_compute_appoint_date_time',    
    ) 
   

    @api.depends('call_request_appointment_date')
    def _compute_appoint_date_time(self):
        for record in self:
            if record.request_date:
                record.appt_created_date = record.call_request_appointment_date.date().strftime("%d-%m-%Y")
                record.appt_created_time = record.call_request_appointment_date.strftime('%H:%M:%S')
    
    cic_ref_no=fields.Char(sting='CIC Ref No')
    work_order_no=fields.Char(sting='Work order no')
    district=fields.Char(sting='District')
  
    
class HrTimesheetSheet(models.Model):
    _inherit = 'account.analytic.line'

#     support_request_id = fields.Many2one(
#         'machine.repair.support',
#         domain=[('is_close','=',False)],
#         string='Machine Repair Support',
#     )
    billable = fields.Boolean(
        string='Chargable?',
        default=True,
    )
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

class View(models.Model):

    _inherit = "ir.ui.view"
    # _inherit = ["ir.ui.view", "website.seo.metadata"]

    visibility = fields.Selection(default='connected')
