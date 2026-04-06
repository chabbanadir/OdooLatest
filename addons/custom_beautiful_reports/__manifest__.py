{
    'name': 'Custom Beautiful Reports',
    'version': '1.0',
    'category': 'Customizations',
    'summary': 'Beautiful and modular QWeb templates for Invoices and Quotes',
    'description': """
        Replaces the default Odoo invoice and sale order templates with a beautifully designed, modern layout.
    """,
    'author': 'Your Name',
    'depends': ['account', 'sale_management'],
    'data': [
        'report/custom_layout.xml',
        'report/invoice_template.xml',
        'report/quote_template.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
