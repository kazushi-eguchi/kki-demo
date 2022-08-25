# -*- coding: utf-8 -*-
# from odoo import http


# class KkiInventory(http.Controller):
#     @http.route('/kki_inventory/kki_inventory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_inventory/kki_inventory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_inventory.listing', {
#             'root': '/kki_inventory/kki_inventory',
#             'objects': http.request.env['kki_inventory.kki_inventory'].search([]),
#         })

#     @http.route('/kki_inventory/kki_inventory/objects/<model("kki_inventory.kki_inventory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_inventory.object', {
#             'object': obj
#         })
