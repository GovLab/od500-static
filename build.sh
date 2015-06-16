#!/bin/bash

python translate.py themes/od500/translations/
pelican -r content/
