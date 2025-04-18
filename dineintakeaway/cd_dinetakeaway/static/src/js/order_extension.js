/** @odoo-module **/

import { Order } from "@point_of_sale/app/store/models";

// Store `takeaway` on the order object
Order.prototype.set_takeaway = function (val) {
    this.takeaway = val;
};

// Add `takeaway` to JSON for syncing
const orderExport = Order.prototype.export_as_JSON;
Order.prototype.export_as_JSON = function () {
    const json = orderExport.apply(this, arguments);
    json.takeaway = this.takeaway || false;
    return json;
};

// Add `takeaway` to printing context
const exportForPrinting = Order.prototype.export_for_printing;
Order.prototype.export_for_printing = function () {
    const print_data = exportForPrinting.apply(this, arguments);
    print_data.takeaway = this.takeaway || false;
    console.log("log>>>>>>>>>>:", print_data.takeaway )
    console.log("log2>>>>>>>>>>:", print_data )
    return print_data;
};

// // Init from JSON if needed
// const orderInit = Order.prototype.init_from_JSON;
// Order.prototype.init_from_JSON = function (json) {
//     orderInit.apply(this, arguments);
//     this.takeaway = json.takeaway || false;
// };
