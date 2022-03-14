from translator import *
import unittest

class TestNull(unittest.TestCase):
    def test1(self):
        self.assertDictEqual(english_text,"")
        self.assertDictEqual(french_text,"")

class TestTranslation(unittest.TestCase):
    def test2(self):
        self.assertDictEqual(english_to_french("Hello"), "Bonjour")
        self.assertDictEqual(french_to_english("Bonjour"), "Hello")
    
if __name__ == '__main__':
    unittest.main()
