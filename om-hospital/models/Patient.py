# noinspection PyUnresolvedReferences
from odoo import models, fields,api ,_


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
    name_sequence = fields.Char(string='Patient Sequence', required=True, copy=False, readonly=True,
                                index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_sequence', _('New')) == _('New'):
            vals['name_sequence'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')

        result = super(HospitalManagement, self).create(vals)
        return result



