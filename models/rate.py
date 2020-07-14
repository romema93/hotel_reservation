# -*- coding: utf-8 -*-

from odoo import models, fields


class Rate(models.Model):
    _name = "hotel_reservation.rate"

    room_id = fields.Many2one("hotel_reservation.room", string="Habitación")
    rate_id = fields.Many2one("hotel_reservation.rate.type", string="Tipo de tarifa")
    date_from = fields.Date(string="Valido desde")
    date_to = fields.Date(string="Valido hasta")
    rate = fields.Monetary(string="Tarifa")
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)

    def search_rate(self, room_id, date_from):
        rate_id = self.search([('date_from', '<=', date_from), ('room_id', '=', room_id.id)])
        if rate_id:
            return rate_id.rate
        return 0
