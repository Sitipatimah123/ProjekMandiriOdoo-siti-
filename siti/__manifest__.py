# -*- coding: utf-8 -*-
{
    'name': "Module SIti Project",

    'summary': """
        Module Project Siti""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],


    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu.xml',
        'views/kelompokbarang_view.xml',
        'views/barang_view.xml',
        'views/person_view.xml',
        'views/kasir_view.xml',
        'views/apoteker_view.xml',
        'views/cleningservice_view.xml',
        'views/pembeli_view.xml',
        'views/pemasok_view.xml',
        'views/direksi_view.xml',
        'views/penjualan_view.xml',
        'report/daftar_pemasokpdf.xml',
        #'wizard/barangdatang_view.xml',



    ],
    # only loaded in demonstration mode
}
