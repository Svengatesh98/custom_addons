
/* @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { Component, useState, useRef } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
// import { CustomAlertPopup } from "@pos_customization/js/popup";

console.log("The File is called");
export class DineInButton extends Component {
  static template = "cd_dinetakeaway.DineInButton";

  setup() {
    this.pos = usePos();
    this.orm = useService("orm");
    this.popup = useService("popup");
    this.state = useState({ dineIn: this.pos.get_order().dine_in || false });
  }
  async click_check_dine(ev) {
    const order = this.pos.get_order();
    if (order.is_empty()) {
      alert("Please add products!!");
      return;
    }
    order.dine_in = !order.dine_in;
    this.state.dineIn = order.dine_in;
    // console.log("Dine-in button clicked", ev);
    console.log("Dine In status:", this.state.dineIn);

    // Only override export once
    if (!order._export_patched) {
      const originalExport = order.export_as_JSON;
      order.export_as_JSON = function () {
        const json = originalExport.apply(this, arguments);
        json.dine_in = this.dine_in || false;
        return json;
      };
      order._export_patched = true;
    }
  }
  export_for_printing() {
    this.state.dineIn = order.dine_in;
    // json.dine_in = this.dine_in;
    console.log('Json>>>>>>>>>:', this.state.dineIn)
    return json;
  }


}

ProductScreen.addControlButton({
  component: DineInButton,
  position: ["after", "OrderlineCustomerNoteButton"],
});

