#!/bin/bash

rm -rf output/
python translate.py themes/od500/translations/
pelican content/
cp output/en/index.html output/index.html
cp -R output/ignore/theme output/theme
cp -R output/ignore/theme output/en/theme
