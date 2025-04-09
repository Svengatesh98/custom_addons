const { Component, useState, xml } = owl;

class CounterComponent extends Component {
    setup() {
        this.state = useState({ count: 0 });
    }
    increment() {
        this.state.count++;
    }
}

CounterComponent.template = xml`
    <div class="counter-container" t-on-click="increment">
        <span>Count: <t t-esc="state.count"/></span>
    </div>
`;

export { CounterComponent };
