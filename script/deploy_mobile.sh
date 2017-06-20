#!/usr/bin/env sh
if [ "$#" != 0 ]; then
  echo "Usage: $0"
  exit 1
fi

DST=../../mobile
./0_generate_pot.py
./1_generate_app.py $DST mobile
./2_update_translation.py $DST mobile all

