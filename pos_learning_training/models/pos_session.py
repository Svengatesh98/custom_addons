# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class PosSession(models.Model):
    _inherit ='pos.session'

    def _pos_ui_models_to_load(self):
        res = super()._pos_ui_models_to_load()
        res.append('pos.learning')
        return res

    def _loader_params_pos_learning(self):
        return {
            'search_params': {
                # 'domain': [('state', '=', 'draft')],
                'fields': ['name', 'code', 'Number','partner_id'],
            }
        }

    def _get_pos_ui_pos_learning(self, params):
        return self.env['pos.learning'].search_read(**params['search_params'])