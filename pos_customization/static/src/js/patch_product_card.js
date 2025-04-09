/** @odoo-module **/

import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
import { patch } from "@web/core/utils/patch";
import { xml } from "@odoo/owl";

patch(ProductCard.prototype, {
    get template() {
        return xml/* xml */ `
            <div class="product-card">
                <div class="product-image">
                    <img t-att-src="props.product.image_url" />
                </div>
                <div class="product-name">
                    <t t-esc="props.product.display_name" />
                </div>

                <div class="product-qty" style="font-size: 13px; color: #333;">
                    Available Qty: <t t-esc="props.product.qty_available || 0" />
                </div>

                <div class="product-price">
                    <t t-esc="env.pos.format_currency(props.product.price)" />
                </div>
            </div>
        `;
    }
});
