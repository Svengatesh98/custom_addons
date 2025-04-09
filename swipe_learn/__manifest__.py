{
    "name": "Swipe Feature in Odoo",
    "version": "1.0",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/swipe_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
           "swipe_learn/static/src/js/swipe.js",
           "swipe_learn/static/src/xml/swipe.xml",
           'swipe_learn/static/src/css/swiper.css',
           
        ],
    },
}
