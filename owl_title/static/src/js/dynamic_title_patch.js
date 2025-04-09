/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { WebClient } from "@web/webclient/webclient";
import { useDynamicTitle } from "../js/dynamic_title";

patch(WebClient.prototype, {
    setup() {
        this._super();
        useDynamicTitle();  // Call our function to update the title dynamically
    },
});
