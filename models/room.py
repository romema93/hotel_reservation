# -*- coding: utf-8 -*-

from odoo import models, fields


class Room(models.Model):
    _name = 'hotel_reservation.room'
    _description = 'Habitaciones'

    number = fields.Integer(string='Numero de habitacion', required=True)
    floor = fields.Integer(string='Piso')
    description = fields.Char(string='Descripcion')
