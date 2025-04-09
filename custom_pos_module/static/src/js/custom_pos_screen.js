// static/src/js/custom_pos_screen.js
import { PaymentScreen } from '@point_of_sale/screens';
import CustomButton from './custom_button';

class CustomPaymentScreen extends PaymentScreen {
    renderElement() {
        super.renderElement();
        const button = new CustomButton();
        button.mount(this.el);  // Mount custom button to the screen
    }
}

const { registry } = require('@web/core/registry');
registry.category('screens').add('CustomPaymentScreen', CustomPaymentScreen);
