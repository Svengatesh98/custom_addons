{
    "name": "Dynamic Tab Title",
    "summary": "Dynamically change browser tab title based on action and record in Odoo 17.ex: Sales Dashboard-(Odoo - Sales-Quation)",
    "version": "17.0.1.0",
    "category": "Web",
    "author": "Vengateshwaran",
    "depends": ["web"],
    "assets": {
        "web.assets_backend": [
              "dynamic_title/static/src/js/tab_title_dynamic.js",
        ],
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
