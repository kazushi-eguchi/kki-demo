# -*- coding: utf-8 -*-

from odoo import models, fields, api


class carsize(models.Model):
    _name = 'car.size'
    _description = 'car.size'

    name = fields.Char()

