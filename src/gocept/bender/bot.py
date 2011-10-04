# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

from gocept.bender.secret import PASSWORD
import Queue
import gocept.bender.http
import gocept.bender.quote
import jabberbot
import logging
import socket
import sys


log = logging.getLogger(__name__)


class Bender(jabberbot.JabberBot):

    muc = 'team@chat.gocept.com'

    def __init__(self):
        super(Bender, self).__init__(
            'ws@gocept.com', PASSWORD, res='bender.' + socket.gethostname())
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


def main():
    global BENDER
    # logging.root.handlers = [logging.StreamHandler(sys.stdout)]
    # logging.root.setLevel(logging.DEBUG)
    BENDER = Bender()
    httpd = gocept.bender.http.HTTPServer.start('localhost', 9090)
    quote = gocept.bender.quote.QuoteTrigger.start(BENDER)
    try:
        BENDER.serve_forever()
    finally:
        httpd.shutdown()
        quote.stop()
