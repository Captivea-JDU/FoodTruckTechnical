# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    
    _name = 'food.course'
    _description = 'Course Info'
    
    name = fields.Char(string='Title', required=True)
    desription = fields.Text(string='Description', required=True)
    
    level = fields.Selection(string='Level',
                            selection=[('beginner', 'Beginner')
                                      ('intermediate', 'Intermediate'),
                                      ('advanced', 'Advanced')]
                            copy=False)
    
    active = fields.Boolean(string='Active', default=True)