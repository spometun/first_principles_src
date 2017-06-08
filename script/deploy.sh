#!/usr/bin/env sh
if [ "$#" -lt 1 ] || [ "$#" -gt 2 ] ; then
  echo "Usage: $0 <destination_path> [--mobile]"
  exit 1
fi
if [ ! -d $1 ]; then
  echo "$1 does not exist"
  exit 1
fi
./build.sh $1 $2
./2_generate_translations.py $1
./copy_server.sh $1
