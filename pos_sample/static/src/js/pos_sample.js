// static/src/js/pos_sample.js
odoo.define('pos_sample.CustomButton', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');

    class CustomButton extends PosComponent {
        async onClick() {
            this.showPopup('ConfirmPopup', {
                title: 'Sample Button Clicked',
                body: 'This is a custom button in the POS interface.',
            });
        }
    }
    CustomButton.template = 'CustomButton';

    ProductScreen.addControlButton({
        component: CustomButton,
        condition: function() {
            return true;
        },
    });

    Registries.Component.add(CustomButton);

    return CustomButton;
});