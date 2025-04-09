{
    'name': 'Custom Company Staff',
    'version': '17.0.1.0.0',
    'summary': 'Custom module to manage company staff with one2many relation',
    'author': 'Your Name',
    'category': 'Human Resources',
    'depends': ['base','report_xlsx'],
    'data': [
        "security/ir.model.access.csv",
        'views/custom_staff_view.xml',
        'report/custom_staff_report_views.xml',
        'report/custom_staff_template.xml',
        # 'report/custom_staff_excel_report_xlsx.xml',
    ],
       'assets': {
        'web.assets_backend': [
        "staff_creation/static/src/css/custom.css",
        ],
        },

    'installable': True,
    'application': False,
}
