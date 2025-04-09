/** @odoo-module */


import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { TextAreaPopup } from "@point_of_sale/app/utils/input_popups/textarea_popup";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";
import { onMounted, useRef, useState } from "@odoo/owl";
import { PosDB } from "@point_of_sale/app/store/db";
import { Order, Orderline, Payment } from "@point_of_sale/app/store/models";
import { ErrorBarcodePopup } from "@point_of_sale/app/barcode/error_popup/barcode_error_popup";

import {
    formatFloat,
    roundDecimals as round_di,
    roundPrecision as round_pr,
    floatIsZero,
} from "@web/core/utils/numbers";

patch(PosStore.prototype, {
    async _processData(loadedData) {
        await super._processData(...arguments);
        this.multi_barcode_options = loadedData['pos.multi.barcode.options'] || [];
        console.log("this.multi_barcode_options:",this.multi_barcode_options)
    },
});

patch(PosDB.prototype, {
    add_products(products) {
        var self = this;
        super.add_products(...arguments);
            for(var i = 0, len = products.length; i < len; i++){
                var product = products[i];
                if(product.pos_multi_barcode_option){
                    var barcode_list = $.parseJSON(product.barcode_options);
                    for(var k=0;k<barcode_list.length;k++){
                        this.product_by_barcode[barcode_list[k]] = product;
                    }
                }
            }
    }
});

patch(Orderline.prototype, {
    setup() {
        super.setup(...arguments);
            this.new_uom = '';
        },
        set_pro_uom(uom_id){
            this.new_uom = this.pos.units_by_id[uom_id];
            // this.trigger('change',this);
        },

        get_unit(){
            var unit_id = this.product.uom_id;
            if(!unit_id){
                return undefined;
            }
            unit_id = unit_id[0];
            if(!this.pos){
                return undefined;
            }
            return this.new_uom == '' ? this.pos.units_by_id[unit_id] : this.new_uom;
        },

        export_as_JSON(){
            var unit_id = this.product.uom_id;
            var json = super.export_as_JSON(...arguments);
            json.product_uom = this.new_uom == '' ? unit_id[0] : this.new_uom.id;
            return json;
        },
        init_from_JSON(json){
            super.init_from_JSON(...arguments);
            this.new_uom = json.new_uom;
        },
    });
patch(ProductScreen.prototype, {
    async _barcodeProductAction(code) {
        const product = await this._getProductByBarcode(code);
        if (!product) {
            return this.popup.add(ErrorBarcodePopup, { code: code.base_code });
        }
        const options = await product.getAddProductOptions(code);
        // Do not proceed on adding the product when no options is returned.
        // This is consistent with clickProduct.
        if (!options) {
            return;
        }

        // Check if the scanned code is a multi-barcode
        var pos_multi_op = this.pos.multi_barcode_options;
        var isMultiBarcode = false;
        for (var i = 0; i < pos_multi_op.length; i++) {
            if (pos_multi_op[i].name == code.code) {
                isMultiBarcode = true;
                break;
            }
        }

        // If it's a multi-barcode, handle it separately
        if (isMultiBarcode) {
            for (var i = 0; i < pos_multi_op.length; i++) {
                if (pos_multi_op[i].name == code.code) {
                    // Create a new order line for the multi-barcode
                    const multiOptions = Object.assign({}, options, {
                        quantity: pos_multi_op[i].qty,
                        price: pos_multi_op[i].price,
                        unit: pos_multi_op[i].unit[0],
                        merge: false, // Ensure a new line is added
                    });
                    this.currentOrder.add_product(product, multiOptions);
                    var line = this.currentOrder.get_last_orderline();
                    line.price_manually_set = true;
                }
            }
        } else {
            // Handle default barcode
            // update the options depending on the type of the scanned code
            if (code.type === "price") {
                Object.assign(options, {
                    price: code.value,
                    extras: {
                        price_type: "manual",
                    },
                });
            } else if (code.type === "weight" || code.type === "quantity") {
                Object.assign(options, {
                    quantity: code.value,
                    merge: false,
                });
            } else if (code.type === "discount") {
                Object.assign(options, {
                    discount: code.value,
                    merge: false,
                });
            }
            // Add the product to the order with the default options
            this.currentOrder.add_product(product, options);
        }

        this.numberBuffer.reset();
    }
});
