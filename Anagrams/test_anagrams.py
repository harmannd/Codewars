from unittest import TestCase
from anagrams import anagrams

class TestAnagrams(TestCase):
    def test_anagrams(self):
        self.assertEqual(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
        self.assertEqual(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
