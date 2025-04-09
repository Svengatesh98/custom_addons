# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'
    
    res_partner_id = fields.Many2one('res.partner', string="default Customer")

    res_customer_ids=fields.Many2many('res.partner',string="Customer")

    # res_partner_id = fields.Many2one('res.partner', string="default Customer")

# related='pos_config_id.res_partner_id
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: