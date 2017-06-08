#!/usr/bin/env sh

DST=../../mobile

./build.sh $DST mobile
./2_generate_translations.py $DST
rm -r $DST/template
