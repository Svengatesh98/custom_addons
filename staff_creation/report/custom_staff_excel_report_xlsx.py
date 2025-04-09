from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError,warnings
from datetime import datetime       
from dateutil.relativedelta import relativedelta
from openpyxl import Workbook
from io import BytesIO

class CustomStaffExcelReport(models.AbstractModel):
    _name = 'report.custom_staff_report.custom_staff_excel_report'
    _description = 'Custom Staff Excel Report'
    _inherit = 'report.report_xlsx.abstract'
    
    
    def _get_report_values(self, docids, data=None):
        docs = self.env['custom.company.staff'].browse(docids)
        doc_args= {
            'doc_ids': docids,
            'doc_model': 'custom.company.staff',
            'docs': docs,
        }
        return self.env['report'].render('custom_staff_report.custom_staff_excel_report', doc_args)

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet("Staff Report") 
        sheet.title = 'Custom Staff Report'
        bold = workbook.add_format({'bold': True})  # Format for headers

    # Writing headers
        sheet.write(0, 0, 'School Name', bold)
        sheet.write(0, 1, 'School Identification Number', bold)
        sheet.write(0, 2, 'Date Of Joining', bold)
        sheet.write(0, 3, 'Number Of Staff', bold)

        row = 1  # Start from second row
        for line in lines:
          sheet.write(row, 0, line.name)  # School Name
          sheet.write(row, 1, line.number)  # School Identification Number
          sheet.write(row, 2, line.doj.strftime('%d-%m-%Y') if line.doj else '')  # Date Of Joining
          sheet.write(row, 3, len(line.staff_line_ids))  # Number Of Staff
          row += 1

        return workbook  # 
        
            
        
    
    

               
        