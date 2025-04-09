/**@odoo-module **/
//import { _t } from "@web/core/l10n/translation";
//import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
//import { useService } from "@web/core/utils/hooks";
//import { Component } from "@odoo/owl";
//import { usePos } from "@point_of_sale/app/store/pos_hook";
//import { CustomAlertPopup } from "@pos_learning/js/custom_popup";
//
//export class CreateButton extends Component {
//
//static template = "pos_learning.CreateButton";
//
//setup() {
//
//this.pos = usePos();
//
//this.popup = useService("popup");
//
//}
//
///**
//
//* Click event handler for the create button.
//
//*/
//
//async onClick() {
//
//this.popup.add(CustomAlertPopup, {
//
//title: _t('Custom Alert'),
//
//body: _t('Choose the alert type')
//
//})
//
//}
//}
///**
// * Add the OrderlineProductCreateButton component to the control buttons in
//   the ProductScreen.
// */
//ProductScreen.addControlButton({
//component: CreateButton,
//});

/**@odoo-module **/
import { _t } from "@web/core/l10n/translation";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { CustomAlertPopup } from "@pos_learning/js/custom_popup";
import { patch } from "@web/core/utils/patch";
patch(PaymentScreen.prototype, {
  async onClick() {
    this.popup.add(CustomAlertPopup, {
      title: _t("Custom Alert"),

      body: _t("Choose the alert type"),
    });
  },
});
