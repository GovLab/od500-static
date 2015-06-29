#!/bin/bash

rm -rf output/
python translate.py themes/od500/translations/
pelican content/
cp output/en/index.html output/index.html
cp -R output/bare/theme output/theme
cp -R output/bare/theme output/en/theme
cp -R output/bare/data output/data
