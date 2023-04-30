# -*- coding: utf-8 -*-
from odoo import api, fields, models

class TaskManager(models.Model):
    _name = 'task.manager'
    _description = 'Task Manager'

    name = fields.Char('Task Name', required=True)
    designation=fields.Many2one('task.designation',string='Designation Name')
    department = fields.Many2one('task.department',string='Department Name')
    description = fields.Text('Description')
    date = fields.Date('Date')
    priority = fields.Selection([('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], required=True, default='low')
    status = fields.Selection([('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done')], required=True, default='new')
    assigned_to_id = fields.Many2one('res.users', string='Assigned to', default=lambda self: self.env.user)
    deadline_date = fields.Date('Deadline Date')


class  TaskDesignation(models.Model):
    _name = 'task.designation'
    _description = 'Task Designation'

    name = fields.Char('Designation Name', required=True)
    description = fields.Text('Description')

class  TaskDeprtment(models.Model):
    _name = 'task.department'
    _description = 'Task Department'

    name = fields.Char('Department Name', required=True)
    description = fields.Text('Description')    
    







