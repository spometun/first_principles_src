cd ../../
URL=http://127.0.0.1:8000/www/studies/en/0_index.html
if which xdg-open > /dev/null
then
  xdg-open $URL &
elif which gnome-open > /dev/null
then
  gnome-open $URL &
fi
python -m SimpleHTTPServer
