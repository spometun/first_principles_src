#!/usr/bin/env sh
if [ "$#" != 2 ] || ([ "$2" != web ] && [ "$2" != mobile ]); then
  echo "Usage: $0 <destination_path> {mobile|web}"
  exit 1
fi
./0_generate_template.py $1 $2
./1_copy_english_template_to_lang.py $1
