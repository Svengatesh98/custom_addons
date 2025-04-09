/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";

patch(PosStore.prototype, {
  async _processData(loadeddata) {
    // Call the original method first to retain the existing functionality
    await super._processData(...arguments);
    this.product_temp = loadeddata["product.product"];
    // console.log("Loaded Products:", this.product_temp);
    // this.product_temp.forEach(product => {
    //   console.log(`Product ID: ${product.id}, Available Quantity: ${product.qty_available}`);
    // });
  },
});

// import { patch } from "@web/core/utils/patch";
// import { PosStore } from "@point_of_sale/app/store/pos_store";
// patch(PosStore.prototype, {
//      async _processData(loadedData) {
//         await super._processData(...arguments);
//         this.pos_learn = loadedData["pos.learn"];
//         console.log("Inside Data",this)

//         },
//         get posName() {
//             return this.config.name;
//         },

// });
