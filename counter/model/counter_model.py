from odoo import models, fields, api

class Counter(models.Model):
    _name = 'counter.counter'  # Ensure this matches XML
    _description = 'Counter Model'

    value = fields.Integer(string="Counter Value", default=0)  # Ensure this field exists

    def increment(self):
        """Increment Counter Value"""
        for record in self:
            record.value += 1

