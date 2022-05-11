# -*- coding: utf-8 -*-

{
    'name': 'Webpay Payment Acquirer',
    'category': 'Accounting',
    'author': 'Daniel Santibáñez Polanco',
    'summary': 'Payment Acquirer: Webpay Implementation',
    'website': 'https://globalresponse.cl',
    'version': "2.0.0",
    'description': """Webpay Payment Acquirer""",
    'depends': [
                'payment',
                'payment_currency',
            ],
        'external_dependencies': {
            'python':[
                'urllib3',
                'transbank',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/webpay.xml',
        'views/payment_acquirer.xml',
        'views/res_config_settings.xml',
        'views/payment_transaction.xml',
        'views/webpay_report.xml',
        'data/webpay.xml',
    ],
    'installable': True,
    'application': True,
}
