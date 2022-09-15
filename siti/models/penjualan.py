from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Penjualan(models.Model):
    _name = 'siti.penjualan'
    _description = 'Penjualan'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(
        string='Tanggal Transaksi',
        default=fields.Datetime.now())
    total_bayar = fields.Integer(
        string='Total Pembayaran',
        compute='_compute_totalbayar')
    detailpenjualan_ids = fields.One2many(
        comodel_name='siti.detailpenjualan',
        inverse_name='penjualan_id',
        string='Detail Penjualan')

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for line in self:
            result = sum(self.env['siti.detailpenjualan'].search(
                [('penjualan_id', '=', line.id)]).mapped('subtotal'))
            line.total_bayar = result
    def write(self, vals):
        for line in self:
            data_asli = self.env['siti.detailpenjualan'].search([('penjualan_id', '=', line.id)])
            print(data_asli)

            for data in data_asli:
                print(str(data.barang_id.name) + " " + str(data.qty) + ' ' + str(data.barang_id.stok))
                data.barang_id.stok += data.qty

        line = super(Penjualan, self).write(vals)

        for line in self:
            data_setelah_edit = self.env['siti.detailpenjualan'].search([('penjualan_id', '=', line.id)])
            print(data_asli)
            print(data_setelah_edit)

            for data_baru in data_setelah_edit:
                if data_baru in data_asli:
                    print(data_baru.barang_id.name + " " + str(data_baru.qty) + ' ' + str(data_baru.barang_id.stok))
                    data_baru.barang_id.stok -= data_baru.qty
                else:
                    pass

        return line
class DetailPenjualan(models.Model):
    _name = 'siti.detailpenjualan'
    _description = 'Detail'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(
        comodel_name='siti.penjualan',
        string='Detail Penjualan')
    barang_id = fields.Many2one(
        comodel_name='siti.barang',
        string='List Barang')
    harga_satuan = fields.Integer(
        string='Harga Satuan',
        onchange='_onchange_barang_id')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.qty * line.harga_satuan

    @api.onchange('barang_id')
    def _onchange_barang_id(self):
        if self.barang_id.harga_jual:
            self.harga_satuan = self.barang_id.harga_jual

    @api.model
    def create(self, vals):
        line = super(DetailPenjualan, self).create(vals)
        if line.qty:
            # Mendapatkan data berdasarkan ID pada barang_id
            self.env['siti.barang'].search(
                [('id', '=', line.barang_id.id)]
            ).write({'stok': line.barang_id.stok - line.qty})

        return line

        @api.ondelete(at_uninstall=False)
        def __ondelete_penjualan(self):
            if self.detailpenjualan_ids:
                penjualan = []
                for line in self:
                    penjualan = self.env['siti.detailpenjualan'].search(
                        [('penjualan_id', '=', line.id)])
                    print(penjualan)

                for ob in penjualan:
                    print(ob.barang_id.name + ' ' + str(ob.qty))
                    ob.barang_id.stok += ob.qty

        def unlink(self):
            if self.detailpenjualan_ids:
                penjualan = []
                for line in self:
                    penjualan = self.env['siti.detailpenjualan'].search(
                        [('penjualan_id', '=', line.id)])
                    print(penjualan)

                for ob in penjualan:
                    print(ob.barang_id.name + ' ' + str(ob.qty))
                    ob.barang_id.stok += ob.qty

            line = super(Penjualan, self).unlink()

        @api.constrains('qty')
        def check_quantity(self):
            for line in self:
                if line.qty < 1:
                    raise ValidationError('Jumlah pembelian harus minimal 1, silahkan input dengan benar!')
                elif line.barang_id.stok < line.qty:
                    raise ValidationError('Stok yang tersedia tidak mencukupi.')
                _sql_constraints = [
                    ('no_nota_unik', 'unique (name)', 'Nomor Nota tidak boleh sama!')
                ]

