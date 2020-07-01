# -*- coding: utf-8 -*-

from odoo import models, fields


class RateType(models.Model):
    _name = "hotel_reservation.rate.type"

    rate_type = fields.Char(string="Nombre", required=True)
    description = fields.Char(string="Descripción")
    active = fields.Boolean(string="Activo", default=True)
