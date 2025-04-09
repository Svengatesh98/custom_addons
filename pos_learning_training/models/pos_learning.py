# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class PosLearning(models.Model):
    _name = "pos.learning"
    _description = "Pos learning"

    name = fields.Char(string='Name')
    code = fields.Char(string='code')
    Number = fields.Float(string='Number')
    partner_id = fields.Many2one('res.partner', 'Customer')
