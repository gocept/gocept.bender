# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import BaseHTTPServer
import gocept.bender.bot
import threading
import urllib2


class HTTPServer(BaseHTTPServer.HTTPServer):
    # shutdown mechanism borrowed from gocept.selenium.static.HTTPServer

    _continue = True

    @classmethod
    def start(cls, host, port):
        server_address = (host, port)
        httpd = cls(server_address, BenderRequestHandler)
        thread = threading.Thread(target=httpd.serve_until_shutdown)
        thread.daemon = True
        thread.start()
        return httpd

    def serve_until_shutdown(self):
        while self._continue:
            self.handle_request()

    def shutdown(self):
        self._continue = False
        # We fire a last request at the server in order to take it out of the
        # while loop in `self.serve_until_shutdown`.
        try:
            urllib2.urlopen(
                'http://%s:%s/die' % (self.server_name, self.server_port),
                timeout=1)
        except urllib2.URLError:
            # If the server is already shut down, we receive a socket error,
            # which we ignore.
            pass
        self.server_close()


class BaseHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        pass


class BenderRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers['content-length'])
        data = self.rfile.read(length)
        gocept.bender.bot.BENDER.say(data)
