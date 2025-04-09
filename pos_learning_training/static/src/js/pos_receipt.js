/** @odoo-module */
import { Order } from "@point_of_sale/app/store/models";
/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";
//import { OrderReceipt } from "@point_of_sale/app/screens/receipt_screen";
import { ReceiptScreen } from "@point_of_sale/app/screens/receipt_screen/receipt_screen";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
import { OrderWidget } from "@point_of_sale/app/generic_components/order_widget/order_widget";
import { omit } from "@web/core/utils/objects";
patch(Order.prototype, {
   export_for_printing() {
       const result = super.export_for_printing(...arguments);
       if (this.get_partner()) {
           result.headerData.partner = this.get_partner();
       }
       console.log('Partner',result)
       return result;
   },
});


patch(ReceiptScreen.prototype,{
omit(...args) {
        return omit(...args);
    }
});
ReceiptScreen.components = {
    ...ReceiptScreen.components,
    Orderline,
    OrderWidget

};
