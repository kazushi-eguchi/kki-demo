# -*- coding: utf-8 -*-

from odoo import models, fields, api


class demo(models.Model):
    _inherit = "sale.order"

    memo = fields.Text(string="memo")
    demo1 = fields.Char("demo1")
    demo2 = fields.Integer()
    demo3 = fields.Date("date")
    demo4 = fields.Datetime("Datetime")
    demo5 = fields.Selection(
        [
            ('male', "Male"),
            ('female', "Female"),
            ('other', "Other"),
        ],
        tracking=True)
    demo6 = fields.Many2one("res.partner")
    demo7 = fields.Many2many("res.partner")
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
