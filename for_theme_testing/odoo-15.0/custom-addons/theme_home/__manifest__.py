{
    'name': 'Home Theme',
    'description': 'MyHome website theme',
    'category': 'Theme',
    'sequence': 1000,
    'version': '1.0',
    'depends': ['base','website'],
    'data': [
        'security/ir.model.access.csv',
        'views/header.xml',
        'views/footer.xml',
        'views/homepage.xml',
        'views/services_page.xml',
        'views/yh_cities.xml',
        'views/yh_carosel.xml',
        'views/menus.xml',
        'views/snippets/property_agent.xml',
        'views/snippets/s_cover_login.xml',
        'views/snippets/new_properties.xml',
        # 'views/snippets/rent_mega_menu.xml',
        'views/snippets/explore_cities.xml',
        'views/snippets/carosel.xml',
        'views/snippets/snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'theme_home/static/src/scss/styles.scss',
            'theme_home/static/src/scss/property_agent.scss',
            'theme_home/static/src/js/explore_cities.js',
            'theme_home/static/src/js/explore_cities_options.js',
            'theme_home/static/src/js/for_carosel.js',
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
