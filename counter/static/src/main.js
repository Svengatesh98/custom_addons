const { mount } = owl;
import { CounterComponent } from "./components/CounterComponent.js";

async function setup() {
    const app = new owl.App(CounterComponent);
    await mount(app, document.querySelector("#counter_app"));
}

setup();
