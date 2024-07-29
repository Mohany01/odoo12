# noinspection PyUnresolvedReferences
from odoo import models, fields


class HospitalManagement(models.Model):
    _name = 'hospital.doctors'
    _description = 'Doctors Record'

    name = fields.Char()
    phone_number = fields.Char()
    date_of_birth = fields.Date()
    country = fields.Char()
    age = fields.Integer()
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ])
