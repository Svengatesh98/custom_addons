from odoo import models,fields,api,_

from datetime import datetime


class Purchaseorder(models.Model):
    _inherit='purchase.order.line'
    
    barcode=fields.Char("barcode")
    
    @api.onchange('product_id')
    def _barcode_code(self):
        for rec in self:
            print("rec.product_id.barcode",rec.product_id.barcode)
            rec.barcode = rec.product_id.barcode         
             
    def _prepare_stock_move_vals(self, picking, price_unit, product_uom_qty, product_uom):
        self.ensure_one()
        self._check_orderpoint_picking_type()
        product = self.product_id.with_context(lang=self.order_id.dest_address_id.lang or self.env.user.lang)
        date_planned = self.date_planned or self.order_id.date_planned
        return {
            # truncate to 2000 to avoid triggering index limit error
            # TODO: remove index in master?
            'name': (self.product_id.display_name or '')[:2000],
            'product_id': self.product_id.id,
            'date': date_planned,
            'barcode':self.product_id.barcode,
            'date_deadline': date_planned,
            'location_id': self.order_id.partner_id.property_stock_supplier.id,
            'location_dest_id': (self.orderpoint_id and not (self.move_ids | self.move_dest_ids)
                and (picking.location_dest_id.parent_path in self.orderpoint_id.location_id.parent_path))
                and self.orderpoint_id.location_id.id or self.order_id._get_destination_location(),
            'picking_id': picking.id,
            'partner_id': self.order_id.dest_address_id.id,
            'move_dest_ids': [(4, x) for x in self.move_dest_ids.ids],
            'state': 'draft',
            'purchase_line_id': self.id,
            'company_id': self.order_id.company_id.id,
            'price_unit': price_unit,
            'picking_type_id': self.order_id.picking_type_id.id,
            'group_id': self.order_id.group_id.id,
            'origin': self.order_id.name,
            'description_picking': product.description_pickingin or self.name,
            'propagate_cancel': self.propagate_cancel,
            'warehouse_id': self.order_id.picking_type_id.warehouse_id.id,
            'product_uom_qty': product_uom_qty,
            'product_uom': product_uom.id,
            'product_packaging_id': self.product_packaging_id.id,
            'sequence': self.sequence,
        }
    
    
class PurchaseOrderdetail(models.Model):
    _inherit = 'purchase.order'
    
    incoterm_location = fields.Char(string='IncoLocation')
    # partner_ref = fields.Char('Vendor Reference', copy=False,required=True,
    #     help="Reference of the sales order or bid sent by the vendor. "
    #          "It's used to do the matching when you receive the "
    #          "products as this reference is usually written on the "
    #          "delivery order sent by your vendor.")
    
    date_order_purchase=fields.Datetime('Date',default=fields.Datetime.now)
