/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";

patch(PosStore.prototype, {
  async _processData(loadeddata) {
    await super._processData(...arguments);
    this.product_temp = loadeddata["product.product"];
    console.log("this",this)
    console.log("barcode", this.product_temp);
  },
});
