# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_purchase(models.Model):
    _inherit = "purchase.order"

    memo = fields.Text()
