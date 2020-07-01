# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HotelRoomBooked(models.Model):
    _name = "hotel_reservation.room.booked"

    booking_id = fields.Many2one("hotel_reservation.booking", string="Reserva")
    room_id = fields.Many2one("hotel_reservation.room", string="Habitación")
    rate = fields.Monetary(string="Precio")
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)
