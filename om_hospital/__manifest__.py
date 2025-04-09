{
    "name" :"Hospital Management System",
    "author":"Software Solutions",
    "License":"LGPL-3",
    "version":"17.0.1.1",
     'depends': ['base','mail',"web",'account','product'],
    'data': [
        "security/ir.model.access.csv",
        'data/data.xml',
        "views/menuitem.xml",
        "views/hospital_doctor_views.xml",
        "views/hospital_patient_views.xml",
        # 'views/sequence.xml',  # Load the sequence
        "views/hospital_prescription_views.xml",
        "views/hospital_medicine_views.xml",
        "views/hospital_appointment_views.xml",
        "views/hospital_patient_tag_view.xml",
        "views/account_move_sales.xml",
        "report/prescription_report_views.xml",
        "report/Prescription_report.xml",
       "report/invoice_report.xml",
    ],
        'assets': {
        'web.assets_backend': [
        "om_hospital/static/css/assets.css",
        
        ],
    },
    'installable': True,
    'application': True,

}