# noinspection PyUnresolvedReferences
from odoo import models, fields, api, _
import datetime
from odoo.odoo.exceptions import ValidationError


class HospitalManagement(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'
    # _log_access = False
    name = fields.Char(required=1, default="New", size=7)
    height = fields.Float(digits=(1, 3))
    phone_number = fields.Char()
    weight = fields.Float()
    date_of_birth = fields.Date()
    country = fields.Char()
    age = fields.Integer(compute='calc_age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ])
    image = fields.Binary()
    name_sequence = fields.Char(string='Patient Sequence', required=True, copy=False, readonly=1,
                                index=True, default=lambda self: _('New'))
    # This is Validation in database [Data Tier]
    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This Name Already Exist')
    ]

    @api.depends('date_of_birth')
    def calc_age(self):
        for record in self:
            if record.date_of_birth:
                date_obj = fields.Date.from_string(record.date_of_birth)
                record.age = datetime.datetime.now().year - date_obj.year

    @api.constrains('height', 'weight')
    def _check_height_weight_validation(self):
        for rec in self:
            if rec.height == 0 or rec.weight == 0:
                raise ValidationError('Please Add valid Number')

    @api.model
    def create(self, vals):
        if vals.get('name_sequence', _('New')) == _('New'):
            vals['name_sequence'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        # this line create the record
        result = super(HospitalManagement, self).create(vals)
        return result

    @api.model
    def search(self, domain, offset=0, limit=None, order=None):
        res = super(HospitalManagement, self).search(domain, offset=0, limit=None, order=None)
        print("Read")
        return res

    def write(self, vals):
        res = super(HospitalManagement, self).write(vals)
        print("Write")
        return res

    def unlink(self):
        res = super(HospitalManagement, self).unlink()
        print("Delete")
        return res




