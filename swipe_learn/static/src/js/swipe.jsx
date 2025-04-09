// /** @odoo-module */
// import { Component, useState } from "@odoo/owl";

// export class SwipeAction extends Component {
//     setup() {
//         this.state = useState({ swiped: null, dragging: false });
//     }

//     onDragStart(event) {
//         this.state.dragging = true;
//         event.dataTransfer.setData("text/plain", this.props.text);
//     }

//     onDragEnd() {
//         this.state.dragging = false;
//     }

//     onDrop(event) {
//         event.preventDefault();
//         this.state.swiped = "dropped";
//         this.trigger("update-status", { status: "dropped" });
//     }

//     onDragOver(event) {
//         event.preventDefault();
//     }
// }

// SwipeAction.template = "swipe_learn.SwipeAction";

/** @odoo-module */
import { Component, useState } from "@odoo/owl";

export class SwipeAction extends Component {
    setup() {
        this.state = useState({ swiped: null });
    }

    onSwipeLeft() {
        console.log("Starred Item");
        this.state.swiped = "starred";
        this.trigger("update-status", { status: "starred" });
    }

    onSwipeRight() {
        console.log("Deleted Item");
        this.state.swiped = "deleted";
        this.trigger("update-status", { status: "deleted" });
    }

    onDragStart(event) {
        event.dataTransfer.setData("text/plain", event.target.innerText);
        event.target.classList.add("dragging");
        console.log("Dragging started", event.target.innerText);
    }

    onDragOver(event) {
        event.preventDefault();
        event.target.classList.add("drag-over");
    }

    onDrop(event) {
        event.preventDefault();
        const data = event.dataTransfer.getData("text/plain");
        event.target.classList.remove("drag-over");
        console.log("Dropped:", data);
        this.state.swiped = "dropped";
        this.trigger("update-status", { status: "dropped" });
    }

    onDragEnd(event) {
        event.target.classList.remove("dragging");
    }
}

SwipeAction.template = "swipe_learn.SwipeAction";

