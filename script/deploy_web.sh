#!/usr/bin/env sh
if [ "$#" != 1 ]; then
  echo "Usage: $0 <destination_path>"
  exit 1
fi
if [ ! -d $1 ]; then
  echo "$1 does not exist"
  exit 1
fi
./build.sh $1 web
./2_generate_translations.py $1

mkdir -p $1/api/
chmod -R 755 $1/api/
cp -r ../server/*.php $1/api/
pwd > $1/api/src_path.txt
cp ../server/index.html $1/
