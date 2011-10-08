# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import Queue
import gocept.bender.http
import gocept.bender.quote
import jabberbot
import logging
import socket
import sys


log = logging.getLogger(__name__)


class Bender(jabberbot.JabberBot):

    def __init__(self, user, password, chatroom):
        super(Bender, self).__init__(
            user, password, res='bender.' + socket.gethostname())
        self.muc = chatroom
        self.join_room(self.muc, 'bender')
        self.messages = Queue.Queue()

    def idle_proc(self):
        try:
            message = self.messages.get_nowait()
        except Queue.Empty:
            return super(Bender, self).idle_proc()
        self.send(self.muc, message, message_type='groupchat')

    def say(self, message):
        self.messages.put(message)


def main(**kw):
    # logging.root.handlers = [logging.StreamHandler(sys.stdout)]
    # logging.root.setLevel(logging.DEBUG)
    bender = Bender(kw['jabber_user'], kw['jabber_password'], kw['chatroom'])
    host, port = kw['http_address'].split(':')
    httpd = gocept.bender.http.HTTPServer.start(
        host, int(port), bender, kw['http_user'], kw['http_password'])
    quote = gocept.bender.quote.QuoteTrigger.start(bender, **kw)
    try:
        bender.serve_forever()
    finally:
        httpd.shutdown()
        quote.stop()
