// static/src/js/custom_button.js
import { useState } from '@odoo/owl';
import { PosComponent } from '@web/core/component';

class CustomButton extends PosComponent {
    constructor() {
        super(...arguments);
        this.state = useState({ label: 'Click Me!' });
    }

    onClick() {
        alert('Custom button clicked!');
    }
}

export default CustomButton;
