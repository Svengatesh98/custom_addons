/** @odoo-module */
import { Component } from "@odoo/owl";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
export class ProductCombosButton extends Component {
    static template = "pos_learning.ProductCombosButton";
    setup() {
        this.pos = usePos();
    }
    async click() {
        this.pos.showScreen("ProductCombosScreen");
    }
}
ProductScreen.addControlButton({
    component: ProductCombosButton,
    condition: function () {
        return true;
    },
});
