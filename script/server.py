#/usr/bin/env python3

from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler
import subprocess
import socketserver

PORT = 8000

PATH_FOR_GITHUB_COMMIT = '/api/new-commit'

class AppRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        SimpleHTTPRequestHandler.__init__(self, *args, **kwargs)

    def do_GET(self, *args, **kwargs):
        print(self.path)
        if self.path == PATH_FOR_GITHUB_COMMIT:
            self.send_response(200)
            self.end_headers()
            self.wfile.write('Hello, world!'.encode('utf-8'))
            print(subprocess.check_output(["git", "pull"]))
        else:
            SimpleHTTPRequestHandler.do_GET(self, *args, **kwargs)

Handler = AppRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Serving at port", PORT)
httpd.serve_forever()
