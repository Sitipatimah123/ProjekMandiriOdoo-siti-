# -*- coding: utf-8 -*-
# from odoo import http


# class Siti(http.Controller):
#     @http.route('/siti/siti/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siti/siti/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siti.listing', {
#             'root': '/siti/siti',
#             'objects': http.request.env['siti.siti'].search([]),
#         })

#     @http.route('/siti/siti/objects/<model("siti.siti"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siti.object', {
#             'object': obj
#         })
