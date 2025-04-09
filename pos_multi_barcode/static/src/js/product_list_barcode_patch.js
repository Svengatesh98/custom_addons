/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ProductsWidget } from "@point_of_sale/app/screens/product_screen/product_list/product_list";
import { usePos } from "@point_of_sale/app/store/pos_hook";

patch(ProductsWidget.prototype, {
    setup() {
        super.setup();
        this.pos = usePos();
    },

    get productsToDisplay() {
        const search = (this.props.search || "").toLowerCase().trim();
        const allProducts = super.productsToDisplay;

        if (!search) {
            return allProducts;
        }

        // Create a set to store all matching product IDs
        const matchedProductIds = new Set();

        // 1. First check regular product fields (name, barcode)
        allProducts.forEach(product => {
            if (product.display_name.toLowerCase().includes(search) || 
                product.barcode?.toLowerCase() === search) {
                matchedProductIds.add(product.id);
            }
        });

        // 2. Check multi-barcode options
        (this.pos.multi_barcode_options || []).forEach(option => {
            if (option.name?.toLowerCase() === search) {
                matchedProductIds.add(option.product_id[0]);
            }
        });

        // Return all matched products in the original order
        return allProducts.filter(product => matchedProductIds.has(product.id));
    },
});
// import { patch } from "@web/core/utils/patch";
// import { ProductsWidget } from "@point_of_sale/app/screens/product_screen/product_list/product_list";
// import { usePos } from "@point_of_sale/app/store/pos_hook";

// console.log("🧩 [PATCH] Starting ProductList patch...");

// patch(ProductsWidget.prototype, {
//     setup() {
//         super.setup();
//         this.pos = usePos();
//         console.log("✅ [PATCHED] ProductList.setup - POS Store hooked");
//     },

//     get productsToDisplay() {
//         const search = (this.props.search || "").toLowerCase().trim();
//         const allProducts = super.productsToDisplay;

//         if (!search) {
//             return allProducts;
//         }

//         // Search multi barcode options
//         const extraMatchedProductIds = new Set();
//         for (const option of this.pos.multi_barcode_options || []) {
//             if (option.name?.toLowerCase().includes(search)) {
//                 const product = this.pos.db.get_product_by_id(option.product_id[0]);
//                 if (product) {
//                     extraMatchedProductIds.add(product.id);
//                     console.log(`🔍 Match: ${option.name} → Product ${product.display_name}`);
//                 }
//             }
//         }

//         const allMatched = new Map();
//         for (const product of allProducts) {
//             allMatched.set(product.id, product);
//         }

//         for (const productId of extraMatchedProductIds) {
//             const product = this.pos.db.get_product_by_id(productId);
//             if (product) {
//                 allMatched.set(product.id, product);
//             }
//         }

//         console.log(`📦 Products to display: ${Array.from(allMatched.values()).length}`);
//         return Array.from(allMatched.values());
//     },
// });
