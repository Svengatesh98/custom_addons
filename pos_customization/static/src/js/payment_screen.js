/**@odoo-module **/
import { _t } from "@web/core/l10n/translation";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { CustomAlertPopup } from "@pos_customization/js/popup";
import { patch } from "@web/core/utils/patch";
patch(PaymentScreen.prototype, {
  async onClick() {
    this.popup.add(CustomAlertPopup, {
      title: _t("Custom Alert"),
      body: _t("Choose the alert type"),
    });
  },
});
