# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_forklift(models.Model):
    _name = 'kki_forklift.lift'
    _description = 'kki_forklift.lift'

    name = fields.Char("name")
    image = fields.Binary("image")
    launch_day = fields.Date("Launch Day")
    vendor = fields.Many2one("res.partner", string="vendor")
    note = fields.Text("note")
    size = fields.Many2one("kki_forklift.size", string="size")
    check_history_ids = fields.One2many(
        comodel_name="kki_forklift.history",
        inverse_name="lift_id",
        string="check history")
    price = fields.Integer("price")
    tax = fields.Float("tax", compute="_get_tax", store=True, Tracking=True)

    @api.depends('price')
    def _get_tax(self):
        for rec in self:
            if rec.price:
                tax = rec.price * 0.1
                rec.tax = tax
            else:
                rec.tax = 0

