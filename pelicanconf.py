# -*- coding: utf-8 -*-

'''
Pelican theme for OD500 '''

#from iso3166 import countries

THEME = 'themes/od500'

SITENAME = "Open Data 500"

JINJA_EXTENSIONS = ['jinja2.ext.i18n']

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

# Country -> category
#CATEGORIES_SAVE_AS = 'index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index_ignore.html'
INDEX_SAVE_AS = 'index_ignore.html'

ARTICLE_URL = '{lang}/{category}/{slug}/'
ARTICLE_SAVE_AS = '{lang}/{category}/{slug}/index.html'

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'en': {
        'THEME_STATIC_DIR': 'en/theme',
    },
    'es': {
        'SITENAME': 'Datos Abiertos 500',
    },
    'it': {
        'SITENAME': '???',
    },
    'kr': {
        'SITENAME': '???',
    },
}

COUNTRIES = {
    'us': {
        'name': u'United States',
        'language': u'en',
    },
    'mx': {
        'name': u'Mexico',
        'language': u'es',
    },
    'it': {
        'name': u'Italy',
        'language': u'it',
    },
    'kr': {
        'name': u'Korea',
        'language': u'kr',
    },
}

#COUNTRIES = countries
