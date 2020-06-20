# -*- coding: utf-8 -*-
# from odoo import http


# class HoteReservation(http.Controller):
#     @http.route('/hote_reservation/hote_reservation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hote_reservation/hote_reservation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hote_reservation.listing', {
#             'root': '/hote_reservation/hote_reservation',
#             'objects': http.request.env['hote_reservation.hote_reservation'].search([]),
#         })

#     @http.route('/hote_reservation/hote_reservation/objects/<model("hote_reservation.hote_reservation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hote_reservation.object', {
#             'object': obj
#         })
