# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HotelRoomBooked(models.Model):
    _name = "hotel_reservation.room.booked"

    booking_id = fields.Many2one("hotel_reservation.booking", string="Reserva")
    room_id = fields.Many2one("hotel_reservation.room", string="Habitación")
    rate = fields.Monetary(string="Precio", compute="_compute_rate", store=True)
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)

    @api.depends('room_id')
    def _compute_rate(self):
        for record in self:
            if record.room_id:
                record.rate = self.env['hotel_reservation.rate'].search_rate(record.room_id,
                                                                             record.booking_id.date_from)
            else:
                record.rate = 0
