# noinspection PyUnresolvedReferences
from odoo import models, fields


class HospitalManagement(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'
    # _log_access = False
    name = fields.Char()
    height = fields.Float()
    phone_number = fields.Char()
    weight = fields.Float()
    date_of_birth = fields.Date()
    country = fields.Char()
    age = fields.Integer()
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ])
    image = fields.Binary()



