/** @odoo-module */

import { PosGlobalState } from "@point_of_sale/app/store/pos_global_state";
import { patch } from "@web/core/utils/patch";

patch(PosGlobalState.prototype, {
    async _processData(loadedData) {
        await super._processData(loadedData);

        // Load restricted customers from POS settings
        this.config.restricted_customer_ids = loadedData["pos.config"][0]?.restricted_customer_ids || [];
        console.log("⚙️ Loaded POS Restricted Customers:", this.config.restricted_customer_ids);
    },
});
