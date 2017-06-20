#!/usr/bin/env sh
if [ "$#" != 1 ]; then
  echo "Usage: $0 <destination_path>"
  exit 1
fi
if [ ! -d $1 ]; then
  echo "$1 does not exist"
  exit 1
fi
./0_generate_pot.py
./1_generate_app.py $1 web
./2_update_translation.py $1 web all



