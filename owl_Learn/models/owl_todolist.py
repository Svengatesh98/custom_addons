from odoo import models, fields

class OwlTodo(models.Model):
    _name = 'owl.todolist'  # This name is important
    _description = 'Owl Todo List App'

    name = fields.Char(string="Task Name")
    completed = fields.Boolean(string="Completed")
    color = fields.Char(string="Color")



