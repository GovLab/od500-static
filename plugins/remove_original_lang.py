'''
Simple plugin that prevents the generation of a static site without a language
path.
'''

from pelican import signals

def remove_bare_site(sender):
    '''
    Remove site of DEFAULT_LANG if it's not in a language folder
    '''
    if not sender.output_path.endswith(sender.settings['DEFAULT_LANG']):
        sender.output_path += '/bare'


def register():
    '''
    Register `remove_bare_site` with Pelican.
    '''
    signals.get_generators.connect(remove_bare_site)
