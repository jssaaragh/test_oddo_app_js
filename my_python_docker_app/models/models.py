# models/models.py
from odoo import models, fields, api

class MyDockerModel(models.Model):
    _name = 'my.docker.model'
    _description = 'My Docker Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

    @api.model
    def create(self, vals):
        record = super(MyDockerModel, self).create(vals)
        # Add custom logic here if needed
        return record