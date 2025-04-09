/** @odoo-module */
import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";
import { _lt } from "@web/core/l10n/translation";
import { onMounted, useRef, useState } from "@odoo/owl";

/**
 * CustomAlertPopup component for displaying custom messages as an alert popup.
 * Inherits from AbstractAwaitablePopup.
 */
export class PosLearningPopup extends AbstractAwaitablePopup {
  static template = "pos_learning.PosLearningPopup";

  //  static props = {
  //        ...AbstractAwaitablePopup.props,
  //        data : {type: Object, optional: true},
  //    };

  static defaultProps = {
    data: { type: Object, optional: true },
    confirmText: _lt("Ok"),
    title: "",

    body: "",
  };
}
