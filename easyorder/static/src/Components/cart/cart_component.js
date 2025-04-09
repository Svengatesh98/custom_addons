// /** @odoo-module **/
import { registry } from "@web/core/registry";
import { getDefaultConfig } from "@web/views/view";
import { Component, useSubEnv,} from "@odoo/owl";

export class EasyOrderProductsShoppingCart extends Component {
  setup() {
    useSubEnv({
      config: {
        ...getDefaultConfig(),
        ...(this.env.config || {}),
      },

    });
    // this.state=useState({
    //   products:[],
    // })
    // this.productsData=useService("easyOrder.getProducts");
  }
  // async getProducts(){
  //   this.state.products=await this.productsData;

  // }
}

EasyOrderProductsShoppingCart.template = "easyorder.EasyOrderProductsShoppingCart";

// Ensure this is properly registered
registry.category("components").add("easyorder.EasyOrderProductsShoppingCart", EasyOrderProductsShoppingCart);

// console.log("EasyOrder registered successfully!");
