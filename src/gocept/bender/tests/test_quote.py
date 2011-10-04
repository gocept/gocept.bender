# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

from gocept.bender.quote import QuoteTrigger
import mock
import unittest


class QuoteTriggerTest(unittest.TestCase):

    def test_should_not_talk_twice_within_time_threshold(self):
        bender = mock.Mock()
        trigger = QuoteTrigger(bender)
        trigger.maybe_say_something()
        trigger.maybe_say_something()
        self.assertEqual(1, bender.say.call_count)
