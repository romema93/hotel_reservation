# -*- coding: utf-8 -*-

from odoo import models, fields


class Room(models.Model):
    _name = 'hotel_reservation.room'
    _description = 'Habitaciones'
    _order = 'floor, number'
    _rec_name = 'number'

    floor = fields.Integer(string="Número de Piso", required=True)
    number = fields.Integer(string="Número de habitación", required=True, copy=False, default=0)
    description = fields.Char(string="Descripción")
    room_type_id = fields.Many2one("hotel_reservation.room.type", string="Tipo de habitación")
    rate_ids = fields.One2many("hotel_reservation.rate", "room_id", string="Tarifas", groups='base.group_system')
    active = fields.Boolean(string="Activo", default=True)

    # fields.Text // tipo de dato string con multilinea
    # fields.Selection // Lista desplegable de opciones
    # fields.Html // Tipo de dato como texto pero con capacidades de etiquetas html
    # fields.Float // Almacenar valores decimales
    # fields.Monetary // Similar al Float pero es especifico para almacenar montos de monedas
    # fields.Date // Almacenar valores de fechas
    # fields.Datetime // Almacena valores de fecha y hora
    # fields.Binary // Almacena strings codificados en base64

    # Atributos especiales

    # name // Char, Text, Many2one es usado por defecto para mostrar el nombre del registro
    # active // Booleano permite activar o desactivar un registro
    # sequence // Integer permite definir el orden de los registros en tipos de vista lista (arlbol) y puede configurarse mediante un drag and drop
    # state // Selection representa los estados de un registro

    # Atributos de Campos

    # string // definir el texto de la etiqueta usada para las vistas
    # default // definir un valor por defecto en la acciones de creacion de un registro
    # size // Define la cantidad de carecteres posibles en los tipos de datos Char
    # translate // Aplicable a Char, Text y Html, define si el valor es traducible
    # help // proporciona un texto de ayuda en forma de tooltips
    # readonly // hacemos que el campo sea de solo lectura
    # required // Forzamos a que el campo sea requerido u obligatorio
    # copy // evitar el copiado de la informacion al momento de duplicar un registro
    # groups // limita el acceso o la visibilidad al atributo por los grupos definidos
    # states //

    # Parametros en una relacion Many2one

    # ondelete // define como actuar cuando de elimina el registro relacionado
    # domain // filtra los registros a mostrar en el modelo relacionado
