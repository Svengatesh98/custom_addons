// /** @odoo-module **/
import { registry } from "@web/core/registry";
import { getDefaultConfig } from "@web/views/view";
import { Component, useSubEnv } from "@odoo/owl";

export class EasyOrderProducts extends Component {
  static props = {
    product: {
      type: Object,
      shape: {
        id: Number,
        name: String,
        list_price: Number,
        standard_price: Number,
        // quantity: { type: Number, default: 0 }, 
        onHandQty: Number, // ✅ Ensure onHandQty is included
        default_code: { type: "", optional: true }, // ✅ Optional if missing in some cases
        image_128: { type: String, optional: true },
      },
    },
    addToCard: Function,
    removeFromCard: Function,
    // sendProductData:Function,
  };
  addToCard() {
    this.props.addToCard(this.props.product.id);
  }
  removeFromCard() {
    this.props.removeFromCard(this.props.product.id);
  }

  setup() {
    useSubEnv({
      config: {
        ...getDefaultConfig(),
        ...(this.env.config || {}),
      },
    });
  }
}

EasyOrderProducts.template = "easyorder.EasyOrderProducts";
// Ensure this is properly registered
registry
  .category("components")
  .add("easyorder.EasyOrderProducts", EasyOrderProducts);

// console.log("EasyOrder registered successfully!");
