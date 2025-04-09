from odoo import models, api
from num2words import num2words

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def amount_to_text_sar(self):
        """Convert Amount Total to Words in SAR (Riyal & Halala)."""
        self.ensure_one()  # Ensure only one record is processed
        amount_total = self.amount_total
        integer_part = int(amount_total)
        decimal_part = round((amount_total - integer_part) * 100)

        # Convert integer part to words and append "Riyal"
        amount_text = num2words(integer_part, lang='en')
        amount_text = amount_text.capitalize() + " Riyal"

        # Convert decimal part (Halala) if exists
        if decimal_part > 0:
            amount_text += f" and {num2words(decimal_part, lang='en')} Halala"

        return f"{amount_text}"  # Add Saudi Riyal symbol

