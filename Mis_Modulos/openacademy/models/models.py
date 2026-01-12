# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class openacademy(models.Model):

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Char(string='Description')

class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
