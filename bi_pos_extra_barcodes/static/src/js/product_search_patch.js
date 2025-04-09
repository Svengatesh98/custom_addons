/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";

patch(ProductScreen.prototype, {
    async _updateSearch(event) {
        const query = event.detail.query.trim();
        let results = this.pos.db.search_product_in_category(0, query);

        if (results.length === 0 && this.pos.extraBarcodeMap[query]) {
            results = [this.pos.extraBarcodeMap[query]];
        }

        this.productList.setProducts(results);
    }
});
