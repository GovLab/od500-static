# -*- coding: utf-8 -*-

'''
Pelican theme for OD500 '''

import json
from slugify import slugify

CACHE_CONTENT = False
#CONTENT_CACHING_LAYER = 'generator'
#LOAD_CONTENT_CACHE = True

GZIP_CACHE = False
WITH_FUTURE_DATES = False

READERS = {
    'csv': None,
    'json': None,
    'zip': None,
    'pdf': None,
}

THEME = 'themes/od500'

SITENAME = "Open Data 500"
SITEURL = "http://localhost:8000/"

PLUGIN_PATHS = ['pelican-plugins', 'plugins']
PLUGINS = ['i18n_subsites', 'remove_original_lang', 'generate_companies', 'copy_bare_themes_data']

JINJA_EXTENSIONS = ['jinja2.ext.i18n']
JINJA_FILTERS = {
    'slugify': slugify
}
I18N_GETTEXT_NEWSTYLE = True
I18N_GETTEXT_LOCALEDIR = 'themes/od500/translations'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_UNTRANSLATED_ARTICLES = 'keep'

STATIC_PATHS = ['data', 'files']

# Country -> category
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index_ignore.html'

ARTICLE_URL = '/{lang}/{category}/{slug}/'
ARTICLE_LANG_URL = '/{lang}/{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

COMPANY_URL = '/{country}/companies/{slug}/'
COMPANY_SAVE_AS = '{country}/companies/{slug}/index.html'
#COMPANY_LANG_SAVE_AS = '{country}/companies/{slug}/index.html'

INDEX_SAVE_AS = 'index_ignore.html'

TIMEZONE = 'America/New_York'

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'en': {},
    'es': {},
    'it': {},
    'kr': {},
}

def states_for_map(stats, country):
    '''
    Return state data for the specified country.
    '''
    try:
        states = [s for s in stats if s['country'] == country][0]['states']
    except IndexError:
        return []
    #abbrev, STATE, VALUE
    #state_counts = []
    state_data = []
    for state in states:
        state_data.append({
            "abbrev":state['abbrev'].encode('utf-8'),
            "STATE":state['name'].encode('utf-8'),
            "VALUE":state['count']
        })
    return state_data


def agencies_for_country(agencies, country):
    '''
    Return top 16 agency data for a country.
    '''
    return sorted(
        [a for a in agencies if a['country'] == country and a['dataType'] == 'Federal'],
        key=lambda a: a.get('usedBy_count', 0), reverse=True
    )[0:16]


COUNTRIES = {
    'us': {
        'name': u'United States',
        'categories': [
            'Business & Legal Services', 'Data/Technology',
            'Education', 'Energy', 'Environment & Weather',
            'Finance & Investment', 'Food & Agriculture',
            'Geospatial/Mapping', 'Governance', 'Healthcare',
            'Housing/Real Estate', 'Insurance', 'Lifestyle & Consumer',
            'Media', 'Research & Consulting', 'Scientific Research',
            'Transportation'],
        'states': {
            "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona",
            "AR": "Arkansas", "CA": "California", "CO": "Colorado",
            "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia",
            "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
            "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KA": "Kansas",
            "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine",
            "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan",
            "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri",
            "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
            "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico",
            "NY": "New York", "NC": "North Carolina", "ND": "North Dakota",
            "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
            "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
            "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas",
            "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington",
            "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming",
            "PR": "Puerto Rico"
        },
    },
    'mx': {
        'name': u'Mexico',
        'categories': [
            'Business Services', 'Data/Technology',
            'Education', 'Energy', 'Environment & Weather',
            'Finance & Investment', 'Food & Agriculture',
            'Geospatial/Mapping', 'Governance', 'Healthcare',
            'Housing/Real Estate', 'Insurance', 'Legal Services',
            'Lifestyle & Consumer', 'Media & Communications',
            'Research & Consulting', 'Scientific Research',
            'Transportation'],
        'states': {
            "AS":"Aguascalientes", "BC":"Baja California",
            "BS":"Baja California Sur", "CC":"Campeche", "CS":"Chiapas",
            "CH":"Chihuahua", "CL":"Coahuila", "CM":"Colima",
            "DF":"Distrito Federal", "DG":"Durango", "GT":"Guanajuato",
            "GR":"Guerrero", "HG":"Hidalgo", "JC":"Jalisco",
            "MC":"Estado de México", "MN":"Michoacán", "MS":"Morelos",
            "NT":"Nayarit", "NL":"Nuevo León", "OC":"Oaxaca", "PL":"Puebla",
            "QT":"Querétaro", "QR":"Quintana Roo", "SP":"San Luis Potosí",
            "SL":"Sinaloa", "SR":"Sonora", "TC":"Tabasco", "TS":"Tamaulipas",
            "TL":"Tlaxcala", "VZ":"Veracruz", "YN":"Yucatán", "ZS":"Zacatecas"
        },
    },
    'it': {
        'name': u'Italy',
    },
    'kr': {
        'name': u'Korea',
    },
    'au': {
        'name': u'Australia',
        'categories': [
            'Business & Legal Services', 'Data/Technology',
            'Education', 'Energy', 'Environment & Weather',
            'Finance & Investment', 'Food & Agriculture',
            'Geospatial/Mapping', 'Mining/Manufacturing',
            'Healthcare', 'Housing/Real Estate', 'Insurance',
            'Lifestyle & Consumer', 'Media', 'Research & Consulting',
            'Telecommunications / ISP\'s', 'Transportation'],
        'states': {
            "ACT":"Australian Capital Territory", "NSW":"New South Wales",
            "NT":"Northern Territory", "QLD":"Queensland",
            "SA":"South Australia", "TAS":"Tasmania", "VIC":"Victoria",
            "WA":"Western Australia"
        }
    },
}

def process_countries():
    '''
    Add additional data to COUNTRIES
    '''
    with open('content/data/agency.json', 'r') as f_agency:
        agencies = json.load(f_agency)

    with open('content/data/company.json', 'r') as f_company:
        companies = json.load(f_company)

    with open('content/data/stats.json', 'r') as f_stats:
        stats = json.load(f_stats)

    for code, country in COUNTRIES.iteritems():
        country['agencies'] = agencies_for_country(agencies, code)
        country['states_for_map'] = json.dumps(states_for_map(stats, code))
        country['companies'] = [c for c in companies if c['country'] == code]

process_countries()
