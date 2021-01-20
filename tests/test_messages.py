import unittest
from messages import MessageProcessor,Message,Kingdom
k_test = Kingdom("XYZ" , "AABC")
class TestMessageProcessor(unittest.TestCase):
    def test_check_for_emblem_for_empty_message(self):
        self.assertFalse(MessageProcessor.check_for_emblem(Message(k_test,""),k_test.emblem))
    def test_check_for_emblem_for_message(self):
        self.assertFalse(MessageProcessor.check_for_emblem(Message(k_test,"AGHLOTH"),k_test.emblem))
        self.assertTrue(MessageProcessor.check_for_emblem(Message(k_test,"EEFG"),k_test.emblem))
        self.assertTrue(MessageProcessor.check_for_emblem(Message(k_test,"AVCDFREEFG"),k_test.emblem))