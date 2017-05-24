#/usr/bin/env python3

from http.server import SimpleHTTPRequestHandler
import socketserver

PORT = 8000

class AppRequestHandler(SimpleHTTPRequestHandler):
    def handle(self, *args, **kwargs):
        super(SimpleHTTPRequestHandler, self).handle(*args, **kwargs);

Handler = AppRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Serving at port", PORT)
httpd.serve_forever()
