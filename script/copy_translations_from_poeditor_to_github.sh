#!/usr/bin/env sh
if [ "$#" != 1 ]; then
  echo "Usage: $0 <language>"
  exit 1
fi
LANG_DIR="../../lang/$1"
if [ ! -d $LANG_DIR ]; then
  echo "$LANG_DIR does not exist"
  exit 1
fi


WEB_HOOK="https://poeditor.com/api/webhooks/github?api_token=5b0d77bc255634323a31af2df41c1388&id_project=106095&language="$1"&operation=export_terms_and_translations"

curl $WEB_HOOK

