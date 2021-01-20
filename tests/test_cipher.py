import unittest
from utils.cipher import Cipher

class TestCipher(unittest.TestCase):

    def test_decrypt_empty_string(self):
        self.assertEqual(Cipher.decrypt("",3),"")
    
    def test_decrypt_string(self):

        self.assertEqual(Cipher.decrypt("ABC",1), "ZAB")
        self.assertEqual(Cipher.decrypt("ABC",26), "ABC")
    
    def test_decrypt_circular_behaviour(self):
        self.assertEqual(Cipher.decrypt("ABC",1), Cipher.decrypt("ABC",27))