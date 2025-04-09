/** @odoo-module **/

import { registry } from "@web/core/registry";

export const getProductsService = {
  dependencies: ["orm"],
  async start(env, { rpc, orm }) {
    const data = await orm.searchRead(
      "product.template",
    //   [],
      [["detailed_type","!=","service"]],
      ["name", "list_price", "standard_price"]
    );
    return data;
  },
};
//add Domain and

//services indentifier

registry.category("services").add("easyOrder.getProducts", getProductsService);
console.log("Service easyOrder.getProducts registered successfully!");
