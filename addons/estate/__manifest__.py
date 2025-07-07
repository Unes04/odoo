{
    'name': 'Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'unes',
    'category': 'Real Estate',
    'description': 'Real Estate Property Management',
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'installable': True,
    'application': True,
}
