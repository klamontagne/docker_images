#!/usr/bin/python3

# Thanks https://gist.github.com/phrawzty/62540f146ee5e74ea1ab

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import logging
import os

class GetHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPRequestHandler.do_GET(self)

Handler = GetHandler
httpd = TCPServer(("", int(os.environ['PORT'])), Handler)

httpd.serve_forever()
