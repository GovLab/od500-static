'''
Re-generate all .mo files from .po files within the directory specified in first arg '''

import polib
import os
import sys


def main(rootpath):
    '''
    Convert all pofiles inside rootpath to mofiles and save them.
    '''
    for basepath, _, files in os.walk(rootpath):
        for filename in files:
            if filename.endswith('.po'):
                popath = os.path.join(basepath, filename)
                pofile = polib.pofile(popath)
                mopath = os.path.join(basepath, filename.replace('.po', '.mo'))
                pofile.save_as_mofile(mopath)
                sys.stderr.write('Converted {} to {}\n'.format(popath, mopath))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        sys.stderr.write('''
Proper usage:

    python translate.py path/to/translations

''')
