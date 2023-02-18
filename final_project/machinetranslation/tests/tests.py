import unittest
from translator import frenchtoenglish, englishtofrench

class Testtranslator(unittest.TestCase):
    def frenchtoenglish(self):
        self.assertEqual(frenchtoenglish(None), None)
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')
    
    def englishtofrench(self):
        self.assertEqual(englishtofrench(None), None)
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')

unittest.main()