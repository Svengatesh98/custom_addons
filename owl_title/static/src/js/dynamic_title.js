/** @odoo-module **/

import { useService } from "@web/core/utils/hooks";
import { onMounted } from "@odoo/owl";

export function useDynamicTitle() {
    const actionService = useService("action");

    onMounted(() => {
        console.log("✅ dynamic_title.js is loaded");

        actionService.bus.on("ACTION_MANAGER:UI-UPDATED", null, () => {
            console.log("🔄 ACTION_MANAGER:UI-UPDATED triggered");

            const action = actionService.currentController?.action;
            console.log("📝 Current Action:", action);

            if (action && action.name) {
                let recordName = action.name || action.res_model;
                let recordId = action.res_id ? ` - ${action.res_id}` : "";

                document.title = `Odoo - ${recordName}${recordId}`;
                console.log("✅ Title updated to:", document.title);
            } else {
                document.title = "Odoo";
                console.log("ℹ️ No action found. Title reset to 'Odoo'.");
            }
        });
    });
}
