/** @odoo-module */
import { Component } from "@odoo/owl";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
export class ProductCustomButton extends Component {
    static template = "pos_learning.ProductCustomButton";
    setup() {
        this.pos = usePos();
    }
    async click() {
        this.pos.showScreen("PosLearningScreen");
    }
}
ProductScreen.addControlButton({
    component: ProductCustomButton,
    condition: function () {
        return true;
    },
});
