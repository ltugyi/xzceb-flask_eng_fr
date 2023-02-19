import unittest
from translator import frenchtoenglish, englishtofrench

class Testtranslator(unittest.TestCase):
    def frenchtoenglish(self):
        self.assertEqual(frenchtoenglish(None), None)
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchtoenglish('Bonjour'), 'Bonjour')
    
    def englishtofrench(self):
        self.assertEqual(englishtofrench(None), None)
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishtofrench('Hello'), 'Hello')

unittest.main()