{
    'name': 'Home Theme',
    'description': 'MyHome website theme',
    'category': 'Theme',
    'sequence': 1000,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/header.xml',
        'views/footer.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'theme_home/static/src/scss/styles.scss'
        ],
        'web._assets_primary_variables': [
            "theme_home/static/src/scss/primary_variables.scss",
        ]
    },

    'snippet_lists': {
    },
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
