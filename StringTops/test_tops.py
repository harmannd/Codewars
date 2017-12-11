from unittest import TestCase
from string_tops import tops

class TestTops(TestCase):
    def test_tops(self):
        self.assertEqual(tops(""), "")
        self.assertEqual(tops("12"), "2")
        self.assertEqual(tops("abcdefghijklmnopqrstuvwxyz12345"), "3pgb")
        self.assertEqual(tops("abcdefghijklmnopqrstuvwxyz1236789ABCDEFGHIJKLMN"), "M3pgb")
