# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': "Gestion de cursos, calendario de sesiones, para instrucciones para la formación de los contactos",

    'description': """
    Gestion de cursos, calendario de sesiones, para instrucciones para la formación de los contactos
    """,

    'author': "Mas que Motor",
    'website': "https://www.fpalanturing.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml'
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/openacademy.xml',
        'demo/demo.xml',
        'views/respartner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'aplication' : True,
}