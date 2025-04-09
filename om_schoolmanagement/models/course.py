from odoo import models, fields

class SchoolCourse(models.Model):
    _name = 'school.course'
    _description = 'School Course'

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text(string="Course Description")
    student_ids = fields.Many2many('school.student', string="Students")
    
