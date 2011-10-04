# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import datetime
import pkg_resources
import random
import threading
import time


class QuoteTrigger(object):

    _continue = True
    min_silence_duration = datetime.timedelta(minutes=5)
    speaking_probability = 1.0 / (10 * 60)

    def __init__(self, bender, **kw):
        self.bender = bender
        self.last_spoken = datetime.datetime.min
        self.quotes = pkg_resources.resource_string(
            self.__class__.__module__, 'quote.txt').splitlines()

        for key in ['min_silence_duration', 'speaking_probability']:
            setattr(self, key, kw.get(key, getattr(self, key)))

    @classmethod
    def start(cls, *args, **kw):
        trigger = cls(*args, **kw)
        thread = threading.Thread(target=trigger.run)
        thread.daemon = True
        thread.start()
        return trigger

    def run(self):
        while self._continue:
            self.maybe_say_something()
            time.sleep(1)

    def stop(self):
        self._continue = False

    @property
    def may_speak(self):
        now = datetime.datetime.now()
        return now > self.last_spoken + self.min_silence_duration

    @property
    def should_speak(self):
        return random.random() < self.speaking_probability

    def maybe_say_something(self):
        if not self.may_speak:
            return
        if self.should_speak:
            self.bender.say(random.choice(self.quotes))
            self.last_spoken = datetime.datetime.now()
