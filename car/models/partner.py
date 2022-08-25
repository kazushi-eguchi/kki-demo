# -*- coding: utf-8 -*-

from odoo import models, fields, api


class partner(models.Model):
    _inherit = "res.partner"

    cars = fields.One2many(
        comodel_name="car.car",
        inverse_name="customer",
        string="car", )
    car_count = fields.Integer("car count", compute="_compute_car_count")

    def _compute_car_count(self):
        for item in self:
            car_count = self.env['car.car'].search_count([('customer', '=', item.name)])
            item.car_count = car_count

    def action_open_car(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Car',
            'res_model': 'car.car',
            'domain': [('customer', '=', self.name)],
            'view_mode': 'tree,form',
            'target': 'current',
            'context': {
                'default_name': self.name,
            }
        }