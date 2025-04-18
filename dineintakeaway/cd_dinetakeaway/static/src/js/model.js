/** @odoo-module */
import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";


patch(Order.prototype, {
    setup() {
        super.setup(...arguments);
        this.dine_in = false;
        this.takeaway = false;
    },

    export_as_JSON() {
        const json = super.export_as_JSON(...arguments);
        json.dine_in = this.dine_in ?? false;
        json.takeaway = this.takeaway ?? false;
        return json;
    },
    
    init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        this.dine_in = json.dine_in ?? false;
        this.takeaway = json.takeaway ?? false;
    },
    
    export_for_printing() {
        const result = super.export_for_printing(...arguments);
        result.dine_in = this.dine_in ?? false;
        result.takeaway = this.takeaway ?? false;
        console.log("export_for_printing:",result)
        return result;
    }
    
});



