/** @odoo-module **/

import { Product } from "@point_of_sale/app/store/models";
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";

// Step 1: Add qty_available to the Product model so it is loaded
Product.extraFields = Product.extraFields || [];
if (!Product.extraFields.includes("qty_available")) {
    Product.extraFields.push("qty_available");
    console.log("✅ qty_available added to Product.extraFields");
} else {
    console.log("ℹ️ qty_available already present in Product.extraFields");
}

// Step 2: Patch PosStore to confirm qty_available is loaded
patch(PosStore.prototype, {
    async _processData(loadedData) {
        await super._processData(...arguments);
        console.log("✅ Product qty_available loaded:");
        if (loadedData['product.product']) {
            loadedData['product.product'].forEach(p => {
                console.log(`${p.display_name} => ${p.qty_available}`);
            });
        }
    },
});
