#/usr/bin/env python3

from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler
import subprocess
import socketserver
import os

PORT = 8000

PATH_FOR_GITHUB_COMMIT = '/api/new-commit'

SCRIPT_DIR = os.path.abspath(os.curdir)
ROOT_DIR = os.path.join(SCRIPT_DIR, '..', '..')
WWW_DIR = os.path.join(ROOT_DIR, 'www')
LANG_DIR = os.path.join(ROOT_DIR, 'lang')

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
        else:
            SimpleHTTPRequestHandler.do_GET(self, *args, **kwargs)

httpd = socketserver.TCPServer(('', PORT), AppRequestHandler)

print("Serving at port", PORT)
httpd.serve_forever()
