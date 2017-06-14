#!/usr/bin/env sh
if [ "$#" != 0 ]; then
  echo "Usage: $0"
  exit 1
fi

DST=../../mobile
./0_generate_templates.py $DST mobile
./1_generate_app.py $DST
./2_update_translations.py $DST
rm -r $DST/template
