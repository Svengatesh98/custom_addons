/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PartnerListScreen } from "@point_of_sale/app/screens/partner_list/partner_list";
import { usePos } from "@point_of_sale/app/store/pos_hook";
console.log("PartnerListScreen is patched")
patch(PartnerListScreen.prototype, {
    setup() {
        super.setup(...arguments);
        this.pos = usePos();
        this.restrictedCustomerIds = this.pos.config.res_customer_ids || [];
        console.log("🚀 Restricted Customer IDs:", this.restrictedCustomerIds);
    },

    get partners() {
        let res = [];

        if (this.state.query && this.state.query.trim() !== "") {
            res = this.pos.db.search_partner(this.state.query.trim());
        } else {
            res = this.pos.db.get_partners_sorted(1000);
        }

        // Filter customers based on POS config
        if (this.restrictedCustomerIds.length) {
            res = res.filter((partner) => this.restrictedCustomerIds.includes(partner.id));
        }

        console.log(" Filtered Partner List:", res);

        // Ensure selected partner appears at the top
        if (this.state.selectedPartner) {
            const index = res.findIndex((p) => p.id === this.state.selectedPartner.id);
            if (index !== -1) res.splice(index, 1);
            res.unshift(this.state.selectedPartner);
        }

        return res;
    },

    async getNewPartners() {
        let domain = [];

        // Apply restriction based on POS config
        if (this.restrictedCustomerIds.length) {
            domain = [["id", "in", this.restrictedCustomerIds]];
        }

        console.log("🔍 Fetching restricted customers with domain:", domain);

        const result = await this.orm.silent.call(
            "pos.session",
            "get_pos_ui_res_partner_by_params",
            [[odoo.pos_session_id], { domain, limit: 30 }]
        );

        return result;
    },
});
