/** @odoo-module */
import { registry } from "@web/core/registry";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import {PosLearningPopup} from "@pos_learning/js/pos_learning_popup";
export class PosLearningScreen extends Component {
    static template = "pos_learning.PosLearningScreen";  // Reference to your template

    setup() {
        super.setup(...arguments);
        this.pos = usePos();
        this.popup = useService("popup");
        this.records = [];  // Initialize the records array

//        this.loadPosLearningRecords();  // Load records when the component is setup
    }

    learningPopup(learning){
    console.log('Learning',learning)
         this.popup.add(PosLearningPopup, {
            data: learning
            })
    }

    getlearning() {
        var List = [];
        console.log('Learning',this.pos.pos_learnig)
        Object.values(this.pos.pos_learnig).forEach(function(learning) {
            List.push({
                id: learning.id,
                name: learning.name,
                code: learning.code,
                Number: learning.Number,
            });
        });
        return List
    }



}
// Register the custom screen to show in POS
registry.category("pos_screens").add("PosLearningScreen", PosLearningScreen);
