# -*- coding: utf-8 -*-
{
    'name': "Hotel Reservation",

    'summary': """
        Sistema hotelero de reservas""",

    'description': """
        Permite realizar las reservas en nuestro hotel
        Se puede realizar la facturacion desde el modulo de reservas
    """,

    'author': "Luis Rodrigo Mejia Mateus",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/hotel_reservation_menus.xml',
        'views/room_type.xml',
        'views/room.xml'
    ],
    'application': True
}