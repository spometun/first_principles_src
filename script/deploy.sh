#!/usr/bin/env sh
if [ "$#" != 2 ] || ([ "$2" != web ] && [ "$2" != mobile ]); then
  echo "Usage: $0 <destination_path> mobile/web"
  exit 1
fi
if [ ! -d $1 ]; then
  echo "$1 does not exist"
  exit 1
fi
./build.sh $1 $2
./2_generate_translations.py $1
./copy_server.sh $1
