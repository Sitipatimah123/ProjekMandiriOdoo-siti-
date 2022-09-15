from odoo import api, fields, models


class Pemasok(models.Model):
    _name = 'siti.pemasok'
    _description = 'New Description'

    name = fields.Char(string='Nama Perushaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    barang_id = fields.Many2many(comodel_name='siti.barang', string='Barang')