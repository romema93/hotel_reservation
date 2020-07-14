from odoo import models, fields, api


class BookingWizard(models.TransientModel):
    _name = 'hotel_reservation.booking.wizard'

    room_type_id = fields.Many2one('hotel_reservation.room.type', string='Tipo de habitacion')
    date_from = fields.Date(string='Fecha de llegada', required=True)
    date_to = fields.Date(string='Fecha de salida', required=True)

    def search_rooms(self):
        if self.room_type_id:
            room_ids = self.env['hotel_reservation.room'].search([('room_type_id', '=', self.room_type_id.id)])
        occupied_rooms = self.env['hotel_reservation.room.booked'].search([
            '|',
            '&',
            ('booking_id.date_from', '<=', fields.Date.to_string(self.date_from)),
            ('booking_id.date_to', '>', fields.Date.to_string(self.date_from)),
            '&',
            ('booking_id.date_from', '<', fields.Date.to_string(self.date_to)),
            ('booking_id.date_to', '>=', fields.Date.to_string(self.date_to)),
        ]).mapped(lambda x: x.room_id)
        rooms_available = room_ids - occupied_rooms
        values = [{'room_id': room.id, 'booking_wizard_id': self.id} for room in rooms_available]
        rooms_wizard_available = self.env['hotel_reservation.booking.detail.wizard'].create(values)
        context = dict(self.env.context or {})
        return {
            'type': 'ir.actions.act_window',
            'name': 'Habitaciones Disponibles',
            'res_model': 'hotel_reservation.booking.detail.wizard',
            'view_mode': 'tree',
            'view_id': self.env.ref('hotel_reservation.booking_detail_wizard_view_tree').id,
            'domain': [('id', 'in', rooms_wizard_available.ids)],
            'readonly': True,
            'target': 'current',
            'context': context
        }


class BookingWizardDetail(models.TransientModel):
    _name = 'hotel_reservation.booking.detail.wizard'

    booking_wizard_id = fields.Many2one('hotel_reservation.booking.wizard')
    room_id = fields.Many2one('hotel_reservation.room')
    room_type_id = fields.Many2one('hotel_reservation.room.type', related='room_id.room_type_id')
    rate = fields.Monetary(string="Tarifa", compute="_compute_rate")
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)

    @api.depends('room_id')
    def _compute_rate(self):
        for record in self:
            if record.room_id:
                record.rate = self.env["hotel_reservation.rate"].search_rate(record.room_id, record.booking_wizard_id.date_from)
            else:
                record.rate = 0