/** @odoo-module **/

import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
import { patch } from "@web/core/utils/patch";

patch(ProductCard.prototype, {
    setup() {
        super.setup();
    },
});

ProductCard.template = `
   <templates id="template" xml:space="preserve">
    <t t-name="point_of_sale.ProductCard" t-inherit-mode="extension" t-inherit="point_of_sale.ProductCard">
      <xpath expr="//div[contains(@class, 'product-price')]" position="after">
        <t t-if="props.product.qty_available !== undefined">
          <div class="product-qty">
            Available Qty: <t t-esc="props.product.qty_available"/>
          </div>
        </t>
      </xpath>
    </t>
  </templates>sss
`;
