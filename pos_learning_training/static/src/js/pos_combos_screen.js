/** @odoo-module */
import { registry } from "@web/core/registry";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { Component } from "@odoo/owl";
export class ProductCombosScreen extends Component {
    static template = "pos_learning.ProductCombosScreen";
    setup() {
        super.setup(...arguments);
        this.pos = usePos();
    }
    getComboList() {
        var comboList = [];
        Object.values(this.pos.db.combo_by_id).forEach(function(combo) {
            comboList.push({
                id: combo.id,
                name: combo.name,
                base_price: combo.base_price,
                combo_line_ids: combo.combo_line_ids,
            });
        });
        return comboList
    }
}
registry.category("pos_screens").add("ProductCombosScreen", ProductCombosScreen);
