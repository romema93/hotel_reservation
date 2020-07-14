# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Booking(models.Model):
    _name = "hotel_reservation.booking"

    guest_id = fields.Many2one("res.partner", string="Huésped", domain="[('guest','=',1)]")
    date_from = fields.Date(string="Fecha de llegada")
    date_to = fields.Date(string="Fecha de salida")
    room_booked_ids = fields.One2many("hotel_reservation.room.booked", "booking_id")
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirm', 'Confirmado'),
        ('cancel', 'Cancelado')
    ])

    @api.model
    def default_get(self, field_names):
        defaults = super(Booking, self).default_get(field_names)
        active_ids = self.env.context.get('active_ids', False)
        active_model = self.env.context.get('active_model', False)
        if active_ids and active_model == 'hotel_reservation.booking.detail.wizard':
            detail = self.env[active_model].browse(active_ids)
            defaults.update({
                'date_from': detail[0].booking_wizard_id.date_from,
                'date_to': detail[0].booking_wizard_id.date_to,
                'room_booked_ids': [
                    (0, 0, {'room_id': x.room_id.id, 'rate': x.rate, 'currency_id': x.currency_id.id}) for x in detail
                ]
            })
        return defaults
