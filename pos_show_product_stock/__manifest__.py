{
    "name": "POS Show Product Stock",
    "version": "1.0",
    "category": "Point of Sale",
    "depends": ["point_of_sale",'stock','base'],
    "assets": {
        'point_of_sale._assets_pos':[
            "pos_show_product_stock/static/src/js/product_qty_model_patch.js",
            # "pos_show_product_stock/static/src/js/product_qty_template_patch.js",
            #  "pos_show_product_stock/static/src/xml/product_card_template.xml",
        ]
    },
    "installable": True,
    "license": "LGPL-3"
}
