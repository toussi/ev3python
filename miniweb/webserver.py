#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
from time import sleep 

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        print "Hello hello"
        # m1.run_timed(..... 
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)



Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)


server.serve_forever()
