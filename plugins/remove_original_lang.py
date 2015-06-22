from pelican import signals

def remove_bare_site(sender):
    '''
    Remove site of DEFAULT_LANG if it's not in a language folder
    '''
    if not sender.output_path.endswith(sender.settings['DEFAULT_LANG']):
        sender.output_path += '/ignore'

def register():
    signals.get_generators.connect(remove_bare_site)
