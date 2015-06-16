# -*- coding: utf-8 -*-

'''
Pelican theme for OD500 '''

THEME = 'themes/od500'

SITENAME = "Open Data 500"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

JINJA_EXTENSIONS = ['jinja2.ext.i18n']
I18N_GETTEXT_NEWSTYLE = True
I18N_GETTEXT_LOCALEDIR = 'themes/od500/translations'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_UNTRANSLATED_ARTICLES = 'keep'

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
    },
    'mx': {
        'name': u'Mexico',
    },
    'it': {
        'name': u'Italy',
    },
    'kr': {
        'name': u'Korea',
    },
    'au': {
        'name': u'Australia',
    },
}
