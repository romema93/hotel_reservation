# -*- coding: utf-8 -*-

from odoo import models, fields


class RoomType(models.Model):
    _name = 'hotel_reservation.room_type'
    _description = 'Tipo de habitacion'

    name = fields.Char(string="Tipo de habitación", required=True)
    description = fields.Text(string='Descripcion')
    active = fields.Boolean(string='Activo')
