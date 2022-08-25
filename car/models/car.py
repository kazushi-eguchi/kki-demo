# -*- coding: utf-8 -*-

from odoo import models, fields, api


class car(models.Model):
    _name = 'car.car'
    _description = 'car.car'

    name = fields.Char()
    number = fields.Char("license plate number", store=True)
    # size = fields.Char('size')
    length = fields.Float('length')
    wide = fields.Float('wide')
    height = fields.Float('height')
    memo = fields.Text()
    image = fields.Binary(string="Image")
    size = fields.Many2one('car.size', string='size')
    customer = fields.Many2one('res.partner', string='customer')
    kyori = fields.Float('')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
