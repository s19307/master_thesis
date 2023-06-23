from odoo import fields, models


class Applicant(models.Model):
    _inherit = 'hr.applicant'

    cv_file = fields.Binary(string='CV File', attachment=True)
