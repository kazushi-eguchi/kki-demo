# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderLineMeno(http.Controller):
#     @http.route('/sale_order_line_meno/sale_order_line_meno/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_line_meno/sale_order_line_meno/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_line_meno.listing', {
#             'root': '/sale_order_line_meno/sale_order_line_meno',
#             'objects': http.request.env['sale_order_line_meno.sale_order_line_meno'].search([]),
#         })

#     @http.route('/sale_order_line_meno/sale_order_line_meno/objects/<model("sale_order_line_meno.sale_order_line_meno"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_line_meno.object', {
#             'object': obj
#         })
