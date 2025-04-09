/** @odoo-module **/
import { Component } from "@odoo/owl";

export class BarcodeScannerWidget extends Component {
    static template = "pos_learning.BarcodeScannerWidget";

    setup() {
        console.log("BarcodeScannerWidget initialized!"); // Debug log to confirm initialization
    }

    barcodeScan() {
        console.log("Button clicked!"); // Debug log for button click
        alert("Scan triggered!"); // Visual confirmation
    }
}
