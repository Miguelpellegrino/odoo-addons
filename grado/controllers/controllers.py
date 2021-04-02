# -*- coding: utf-8 -*-
from odoo import http

# class GradoI(http.Controller):
#     @http.route('/grado_i/grado_i/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/grado_i/grado_i/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('grado_i.listing', {
#             'root': '/grado_i/grado_i',
#             'objects': http.request.env['grado_i.grado_i'].search([]),
#         })

#     @http.route('/grado_i/grado_i/objects/<model("grado_i.grado_i"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('grado_i.object', {
#             'object': obj
#         })