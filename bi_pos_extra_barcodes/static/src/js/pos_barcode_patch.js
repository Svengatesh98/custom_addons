/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PosGlobalState } from "@point_of_sale/app/store/pos_global_state";

patch(PosGlobalState.prototype, {
    async _processData(loadedData) {
        await this._super(...arguments);

        this.extraBarcodeMap = {};

        for (const product of this.db.get_product_by_id()) {
            if (product.extra_barcodes_ids) {
                for (const extra of product.extra_barcodes_ids) {
                    if (extra && extra.name) {
                        if (extra.name !== product.barcode) {
                            this.extraBarcodeMap[extra.name] = product;
                        }
                    }
                }
            }
        }
    }
});
