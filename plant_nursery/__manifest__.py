# -*- coding: utf-8 -*-
{
    'name': "plant_nursery",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'version': '1.0',
    'category': 'Tools',
    'summary': "Plants and customers managment",
    'description': "Module to manage plants and customers, plants list, manage orders and keep a customers list",
    'author': "Juan David Gonzalez",
    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/nursery_views.xml',
        'views/customer_views.xml',
        'views/nursery_order_views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'css':[],
    'auto_install': False,
    'application': True,
}