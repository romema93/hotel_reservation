# -*- coding: utf-8 -*-

from odoo import models, fields


class Booking(models.Model):
    _name = "hotel_reservation.booking"

    guest_id = fields.Many2one("res.partner", string="Huésped", domain="[('guest','=',1)]")
    date_from = fields.Date(string="Fecha de llegada")
    date_to = fields.Date(string="Fecha de salida")
    room_booked_ids = fields.One2many("hotel_reservation.room.booked", "booking_id")
