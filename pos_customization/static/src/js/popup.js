/** @odoo-module */
import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";
import { _lt } from "@web/core/l10n/translation";
import { onMounted, useRef, useState } from "@odoo/owl";

export class CustomAlertPopup extends AbstractAwaitablePopup {

  setup(){
    console.log("CustomAlertPopup");
  }
  static template = "pos_customization.CustomPopup";

  static defaultProps = {
    title: "",
    body: "",
    confirmText: _lt("Ok"),
   
 
  };

  
}
