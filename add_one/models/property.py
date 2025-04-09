from odoo import models,fields,api
from odoo.exceptions import ValidationError



class property(models.Model):
   _name='property'
   _inherit = ['mail.thread', 'mail.activity.mixin',]
   

   name=fields.Char(required=True,default='new')
   description =fields.Text(tracking=1)
   postcode=fields.Char()
   date_availabilty=fields.Date(tracking=1)
   expected_price=fields.Float(digits=(0,2))
   selling_price=fields.Float(digits=(0,2))
   diff=fields.Float(compute='_compute_diff',store=1,readonly=0)
   bedrooms=fields.Integer(string="Bedrooms", required=True)
   living_area=fields.Integer()
   facades=fields.Integer()
   garage=fields.Boolean()
   garden=fields.Boolean()
   graden_area=fields.Integer()
   garden_oriention=fields.Selection([
      ('north','North'),
      ('south','South'),
      ('east','East'),
      ('west','West'),
   ],default='north')
    
   owner_id=fields.Many2one('owner')
   tag_ids=fields.Many2many('tag')
   owner_address=fields.Char(related='owner_id.address')
   owner_phone=fields.Char(related='owner_id.phone')
    
   state=fields.Selection([
      ('draft','Draft'),
      ('pending','Pending'),
      ('sold','Sold'),
      ('closed','Closed')
    ],default='draft')
   
   line_ids=fields.One2many('property.line','property_id')
    
   _sql_constraints = [
   ("unique_name", "UNIQUE(name)", "This name already exists!")
   ]
   @api.constrains('bedrooms')
   def _check_bedrooms_greater_Zero(self):
      for rec in self:
         if rec.bedrooms <= 0:
            raise ValidationError("Please add a Valid number of bedrooms")
         
   def action_draft(self):
      for rec in self:
         print('Inside draft action')
         rec.state ='draft'  
         # rec.write({
         #    'state':'draft'
         # })  
   def action_pending(self):
      for rec in self:
         print('inside Pending Action')
         rec.write({
            'state':'pending'
         })
   def action_sold(self):
      for rec in self:
         print('inside sold Action')
         rec.state='sold'
         # rec.write({
         #    'state':'sold'
         # })    
   def action_closed(self):
      for rec in self:
         print('inside closed Action')
         rec.state='closed'
         # rec.write({
         #    'state':'sold'
         # })            
   @api.depends('expected_price','selling_price','owner_id.phone')        
   def _compute_diff(self):
      for rec in self:
         print("Inside")
         rec.diff=rec.expected_price - rec.selling_price
         
   @api.onchange('expected_price','owner_id.phone')      
   def _onchange_expected_price(self):
      for rec in self:
         print(rec)
         print("Inside _onchange_expected_price method")
         return{
            'warning':{'title':'warning','message':'negative value.','type':'notification'}
         }
         
         
   
class propertyLine(models.Model):
   _name='property.line'
   # _inherit = ['mail.thread', 'mail.activity.mixin',]      
   
   property_id=fields.Many2one('property')
   area=fields.Float()
   description=fields.Char()
   
   
   def xlsreport(self):
      print("Excel data is printed")
      return True
   
   
               
         

         
         
         
         
          
          



    