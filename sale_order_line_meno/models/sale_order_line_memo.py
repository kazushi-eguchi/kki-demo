# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sale_order_line_meno(models.Model):
    _inherit = "sale.order.line"

    x_note = fields.Text("note")

