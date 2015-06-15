'''
Pelican theme for OD500
'''

THEME = 'themes/od500'
SITENAME = "Open Data 500"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

ARTICLE_URL = '{lang}/{category}/{slug}/'
ARTICLE_SAVE_AS = '{lang}/{category}/{slug}/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'en': {
    },
    'es': {
        'SITENAME': 'el Open Data 500',
    },
    'it': {
        'SITENAME': 'Open Data 500 it',
    },
    'ko': {
        'SITENAME': '???',
    },
}
