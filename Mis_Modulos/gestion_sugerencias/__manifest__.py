{
    'name': 'Gestión de Sugerencias',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Marcos Molis Zapata',
    'category': 'Tools',
    'description': 'Módulo para gestionar un cuaderno de sugerencias.',
    'data': [
        'security/ir.model.access.csv',
        'views/sugerencia_views.xml',
        'reports/sugerencia_report.xml',
    ],
    'installable': True,
    'application': True,
}