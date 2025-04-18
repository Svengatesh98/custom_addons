/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { Component, useState } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";

export class TakeAwayButton extends Component {
    static template = "cd_dinetakeaway.TakeAwayButton";

    setup() {
        this.pos = usePos();
        this.popup = useService("popup");
        this.state = useState({ takeaway: this.pos.get_order()?.takeaway || false });
    }

    async click_check_takeaway() {
        const order = this.pos.get_order();
        order.takeaway = !order.takeaway;
        this.state.takeaway = order.takeaway;
        console.log("Takeaway status:", order.takeaway);
    }
}

ProductScreen.addControlButton({
    component: TakeAwayButton,
    position: ["after", "DineInButton"],
});












// /* @odoo-module **/
// import { _t } from "@web/core/l10n/translation";
// import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
// import { useService } from "@web/core/utils/hooks";
// import { Component,useState } from "@odoo/owl";
// import { usePos } from "@point_of_sale/app/store/pos_hook";
// // import { CustomAlertPopup } from "@pos_customization/js/popup";
// console.log("The File is called")
// export class TakeAwayButton extends Component {
//   static template = "cd_dinetakeaway.TakeAwayButton";
//   setup() {
//     this.pos = usePos();
//     this.popup = useService("popup");
//     this.state = useState({ takeaway: this.pos.get_order().takeaway || false });
//   }
//   async click_check_takeaway() {
//     const order = this.pos.get_order();
//     order.takeaway = !order.takeaway;
//     const orderData = order.export_as_JSON();
//     this.state.takeaway = order.takeaway;
//     console.log("Takeaway status:", this.state.takeaway);
//     console.log("Order details in JSON format:", orderData);
//     const originalExport = order.export_as_JSON;
//     order.export_as_JSON = function () {
//       const json = originalExport.apply(this, arguments);
//       json.takeaway = this.takeaway || false;
//       console.log("data ==================:",json )
//       return json;
//     };
//   }
//   // async onClick() {
//   //   this.popup.add(CustomAlertPopup, {
//   //     title: _t("Custom Alert"),
//   //     body: _t("Choose the alert type"),
//   //   });
//   // }
// }
// ProductScreen.addControlButton({
//   component: TakeAwayButton,
// });