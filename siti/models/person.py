from odoo import api, fields, models

class Person(models.Model):
    _name = 'siti.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')

class Kasir(models.Model):
    _name = 'siti.kasir'
    _inherit = 'siti.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')

class Apoteker(models.Model):
    _name = 'siti.apoteker'
    _inherit = 'siti.person'
    _description = 'New Description'

    id_apoteker = fields.Char(string='ID Apoteker')

class Cleningservice(models.Model):
    _name = 'siti.cleningservice'
    _inherit = 'siti.person'
    _description = 'New Description'

    id_cleningservice = fields.Char(string='ID cleningservice')