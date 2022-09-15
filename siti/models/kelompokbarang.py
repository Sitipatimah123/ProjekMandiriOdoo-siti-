from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'siti.kelompokbarang'
    _description = 'New Description'

    name = fields.Char(string='Nama Kelompok Obat')
    kode_kelompok = fields.Char(string='Kode Kelompok')
    kode_rak = fields.Char(string='Kode Rak')


# Perubahannya from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'siti.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('Obat Pil', 'Obat Jenis Pil'),
        ('Obat Sirup', 'Obat Jenis Sirup'),
        ('Obat Untuk Anak-Anak', 'Obat Untuk Anak-Anak '),
        ('Vitamin', 'Vitamin'),
        ('Alat Medis', 'Alat Medis'),


    ], string='Nama Kelompok Obat ')

    kode_kelompok = fields.Char(string='Kode Kelompok Obat')

    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if self.name == 'Obat Jenis Pil':
            self.kode_kelompok_obat = 'OP1'
        elif self.name == 'Obat Jenis Sirup':
            self.kode_kelompok_obat = 'OS1'
        elif self.name == 'Obat Untuk Anak-Anak':
            self.kode_kelompok_obat = 'OA1'
        elif self.name == 'Vitamin':
            self.kode_kelompok_obat = 'V1'
        elif self.name == 'Alat Medis':
            self.kode_kelompok_obat = 'AM1'

    kode_rak = fields.Char(string='Kode Rak Obat')
    barang_ids = fields.One2many(comodel_name='siti.barang',
                                 inverse_name='kelompokbarang_id',
                                 string='Daftar Obat')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah')

    # Perubahannya di sini
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['siti.barang'].search([('kelompokbarang_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a

    daftar = fields.Char(string='Daftar isi')
    barang_ids = fields.One2many(comodel_name='siti.barang',
                                 inverse_name='kelompokbarang_id',
                                 string='Daftar Obat')