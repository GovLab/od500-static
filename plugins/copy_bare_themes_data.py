'''
Simple plugin that copies theme and data directories from output/bare to root
output/.
'''

from pelican import signals

import os
import polib
import shutil
import sys


def translate(sender):
    '''
    Re-do translations in the theme.
    '''
    for basepath, _, files in os.walk(os.path.join(sender.theme, 'translations')):
        for filename in files:
            if filename.endswith('.po'):
                popath = os.path.join(basepath, filename)
                pofile = polib.pofile(popath)
                mopath = os.path.join(basepath, filename.replace('.po', '.mo'))
                pofile.save_as_mofile(mopath)
                sys.stderr.write('Converted {} to {}\n'.format(popath, mopath))


def copy_and_replace_dir(src, dest):
    '''
    Copy folder at src to dest, replacing anything already there.
    '''
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def copy_bare_themes_data(sender):
    '''
    Copy data and themes from output/bare to output/
    '''
    if not sender.output_path.endswith(sender.settings['DEFAULT_LANG']):
        join = os.path.join
        bare_path = sender.output_path
        root_path = os.path.join(sender.output_path, '../')

        #cp output/en/index.html output/index.html
        shutil.copy2(join(root_path, 'en', 'index.html'), join(root_path))

        #cp -R output/bare/theme output/theme
        copy_and_replace_dir(join(bare_path, 'theme'), join(root_path, 'theme'))

        #cp -R output/bare/theme output/en/theme
        copy_and_replace_dir(join(bare_path, 'theme'), join(root_path, 'en', 'theme'))

        #cp -R output/bare/data output/data
        copy_and_replace_dir(join(bare_path, 'data'), join(root_path, 'data'))

        copy_and_replace_dir(join(bare_path, 'files'), join(root_path, 'files'))


def register():
    '''
    Register `copy_bare_themes_data` with Pelican.
    '''
    #signals.initialized.connect(translate)
    signals.finalized.connect(copy_bare_themes_data)
