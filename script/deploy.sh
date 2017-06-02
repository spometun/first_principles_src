#!/usr/bin/env sh
if [ "$#" != 1 ]; then
  echo "Usage: $0 <destination_path>"
  exit 1
fi
./build.sh $1
./2_generate_translations.py $1
./copy_server.sh $1
