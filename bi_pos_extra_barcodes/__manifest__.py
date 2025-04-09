{
    "name": "POS Extra Barcodes",
    "version": "1.0",
    'author': 'Vengateshwaran.S',
    "category": "Point of Sale",
    "depends": ["point_of_sale", "product"],
    "assets": {
        "point_of_sale._assets_pos": [
            "bi_pos_extra_barcodes/static/src/js/pos_barcode_patch.js",
            "bi_pos_extra_barcodes/static/src/js/product_search_patch.js",
        ],
    },
    "data": [
        "views/pos_product_views.xml",
    ],
    "installable": True,
    "application": False,
}
