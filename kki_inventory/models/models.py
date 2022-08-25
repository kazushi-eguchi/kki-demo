# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_inventory(models.Model):
    _inherit = "stock.picking"

    memo = fields.Text()
    note = fields.Char(string="note")
    x_date = fields.Date("日付")
    x_time = fields.Datetime("日時")
    x_int = fields.Integer("整数")
    x_float = fields.Float("少数")
    x_boolean = fields.Boolean("真偽値")
    x_slection = fields.Selection([
        ('1', 'いち'),
        ('2', 'に'),
        ('3', 'さん'),
        ('4', 'よん'),
    ], default='',
        string="選択", )
    x_m2o = fields.Many2one("res.partner")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
