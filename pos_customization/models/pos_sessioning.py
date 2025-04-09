# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class PosSession(models.Model):
    _inherit ='pos.session'

    def _pos_ui_models_to_load(self):
        res = super()._pos_ui_models_to_load()
        res.append('pos.learn')
        return res

    def _loader_params_pos_learn(self):
        return {
            'search_params': {
                # 'domain': [('state', '=', 'draft')],
                'fields': ['name', 'code', 'Number','partner_id'],
            }
        }

    def _get_pos_ui_pos_learn(self, params):
        return self.env['pos.learn'].search_read(**params['search_params'])
    

    # def _loader_params_product_product(self):
    #     result = super()._loader_params_product_product()
    #     result['search_params']['fields'].append('qty_available')
    #     return result