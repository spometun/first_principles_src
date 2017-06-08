#!/usr/bin/env sh
if [ "$#" -lt 1 ] || [ "$#" -gt 2 ] ; then
  echo "Usage: $0 <destination_path> [--mobile]"
  exit 1
fi
./0_generate_template.py $1 $2
./1_copy_english_template_to_lang.py $1
