#!/usr/bin/env sh
if [ "$#" != 1 ]; then
  echo "Usage: $0 <destination_path>"
  exit 1
fi
./0_generate_template.py $1
./1_copy_english_template_to_lang.py $1
