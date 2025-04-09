from odoo import fields,models

class SchoolEnrollment(models.Model):
    _name = 'school.enrollment'
    _description = 'School Enrollment'

    student_id = fields.Many2one('school.student', string="Student", required=True)
    course_id = fields.Many2one('school.course', string="Course", required=True)
    enrollment_date = fields.Date(string="Enrollment Date", default=fields.Date.today)
