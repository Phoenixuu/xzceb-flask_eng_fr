from translator import *
import unittest

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english("test"),"")
        self.assertEqual(french_to_english("Bonjour"),"Hello")

class TestEnglishToFriend(unittest.TestCase):
    def test2(self):
        self.assertDictEqual(english_to_french("Hello"), "Bonjour")
        self.assertDictEqual(english_to_french("Bonjour"), "Hello")
    
unittest.main()
