from odoo import api, fields, models

class Barang(models.Model):
    _name = 'siti.barang'
    _description = 'New Description'

    name = fields.Char(string='Nama Obat')
    harga_beli = fields.Integer(string='Harga Modal', required=True)
    harga_jual = fields.Integer(string='Harga Jual', required=True)
    # Perubahannya ada di sini ada perubahan lagi
    kelompokbarang_id = fields.Many2one(comodel_name='siti.kelompokbarang',
                                        string='Kelompok',
                                        ondelete='cascade')
    pemasok_id = fields.Many2many(comodel_name='siti.pemasok', string='Pemasok')
    stok = fields.Integer(string='Stok')
