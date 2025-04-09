/**@odoo-module **/
import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { CustomAlertPopup } from "@pos_customization/js/popup";
export class CreateButton extends Component {
  static template = "pos_customization.CreateButton";
  setup() {
    this.pos = usePos();
    this.popup = useService("popup");
  }
  async onClick() {
    this.popup.add(CustomAlertPopup, {
      title: _t("Custom Alert"),
      body: _t("Choose the alert type"),
    });
  }
}
ProductScreen.addControlButton({
  component: CreateButton,
});
