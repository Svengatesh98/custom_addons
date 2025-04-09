from odoo import models,fields,api,_

class ReportHospitalPrescription(models.AbstractModel):
    _name = 'report.prescription'
    _description = 'Prescription Report'

    @api.model
    def get_report_values(self, docids, data=None):
        # Fetch the prescriptions and their related data (patient, doctor, and medicines)
        prescriptions = self.env['hospital.prescription'].browse(docids)
        result = []

        for prescription in prescriptions:
            # Collect patient details
            patient_name = prescription.patient_id.name
            patient_dob = prescription.patient_id.date_of_birth
            patient_age = prescription.patient_id.age
            
            # Collect doctor details
            doctor_name = prescription.doctor_id.name
            doctor_specialty = prescription.doctor_id.specialty

            # Collect the medicines prescribed
            medicines = []
            for medicine in prescription.medicine_ids:
                medicines.append({
                    'medicine_name': medicine.name,
                    'medicine_description': medicine.description,
                    'medicine_dosage': medicine.dosage
                })
            
            result.append({
                'prescription_number': prescription.name,
                'patient_name': patient_name,
                'patient_dob': patient_dob,
                'patient_age': patient_age,
                'doctor_name': doctor_name,
                'doctor_specialty': doctor_specialty,
                'medicines': medicines,
                'prescription_date': prescription.date,
                'instructions': prescription.instructions,
            })
        
        return {
            'doc_ids': docids,
            'doc_model': 'hospital.prescription',
            'data': result
        }
