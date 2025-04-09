# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _


class ResConfigSettings(models.TransientModel):
	_inherit = 'res.config.settings'

	pos_res_partner_id = fields.Many2one('res.partner', related='pos_config_id.res_partner_id', domain="[('id', 'in', customer_ids)]", readonly=False)
   
	customer_ids=fields.Many2many(related='pos_config_id.res_customer_ids', readonly=False)
    
	@api.onchange('customer_id')
	def _onchange_customer_id(self):
      
		if self.customer_ids:
            # If current pos_res_partner_id is not in selected customer_id, reset it
			if self.pos_res_partner_id not in self.customer_ids:
				 self.pos_res_partner_id = self.customer_ids[0]  # Set first selected customer
            # else:	
		    # self.pos_res_partner_id = False 
     
    
    
    
    
 


	

	