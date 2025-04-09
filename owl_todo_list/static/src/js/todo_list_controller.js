/** @odoo-module */

import { ListController } from "@web/views/list/list_controller";
import { registry } from "@web/core/registry";
import { listView } from "@web/views/list/list_view";

export class odooOwlListController extends ListController {
    setup() {
        super.setup();
        // // Pass the method down to the buttons component
        // this.props.triggerShowCustomers = this.showCustomers.bind(this);
    }

    showCustomers() {
        this.actionService.doAction({
            type: "ir.actions.act_window",
            res_model: "res.partner",
            name: "Customers",
            view_mode: 'tree',
            views: [
                [false, "tree"],
                // [false, "form"],
            ],
            target: "current",
            res_id: false,
        });
    }
}

// Register the modified list controller
const viewRegistry = registry.category("views");
export const OwlListController = {
    ...listView,
    Controller: odooOwlListController,
};
viewRegistry.add("odoo_owl_list_controller", OwlListController);
