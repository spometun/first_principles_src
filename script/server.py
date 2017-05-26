#/usr/bin/env python3

from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler
import subprocess
import socketserver
import os
import urllib.request

PORT = 8000

PATH_FOR_GITHUB_COMMIT = '/api/new-commit'
PATH_FOR_POEDITOR_COMMIT = '/api/update-content/'

SCRIPT_DIR = os.path.abspath(os.curdir)
ROOT_DIR = os.path.join(SCRIPT_DIR, '..', '..')
WWW_DIR = os.path.join(ROOT_DIR, 'www')
LANG_DIR = os.path.join(ROOT_DIR, 'lang')

POEDITOR_COMMIT_URLS = {
  'ua': 'https://poeditor.com/api/webhooks/github?api_token=5b0d77bc255634323a31af2df41c1388&id_project=106095&language=uk&operation=export_terms_and_translations',
  'ru': 'https://poeditor.com/api/webhooks/github?api_token=5b0d77bc255634323a31af2df41c1388&id_project=106095&language=ru&operation=export_terms_and_translations',
};

os.chdir(WWW_DIR)

def update_pages():
    os.chdir(LANG_DIR)
    subprocess.call(["git", "pull"])
    os.chdir(SCRIPT_DIR)
    subprocess.call(["sh", "run_all.sh"])

class AppRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        SimpleHTTPRequestHandler.__init__(self, *args, **kwargs)

    def do_GET(self, *args, **kwargs):
        print(self.path)
        if self.path == PATH_FOR_GITHUB_COMMIT:
            self.send_response(200)
            self.end_headers()
            self.wfile.write('Hello, world!'.encode('utf-8'))
            update_pages()
        elif self.path.startswith(PATH_FOR_POEDITOR_COMMIT):
            self.send_response(200)
            self.end_headers()
            self.wfile.write('Hello, world!'.encode('utf-8'))
            language = self.path[len(PATH_FOR_POEDITOR_COMMIT):]
            urllib.request.urlopen(POEDITOR_COMMIT_URLS[language]).read()
        else:
            SimpleHTTPRequestHandler.do_GET(self, *args, **kwargs)

httpd = socketserver.TCPServer(('', PORT), AppRequestHandler)

print("Serving at port", PORT)
httpd.serve_forever()
