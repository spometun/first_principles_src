#!/usr/bin/env sh
if [ "$#" != 1 ]; then
  echo "Usage: $0 <destination_path>"
  exit 1
fi
mkdir -p $1/api/
cp -r ../server/*.php $1/api/
cp ../server/index.html $1/
