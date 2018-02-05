from unittest import TestCase
from non_even_substrings import solve

class TestSequence(TestCase):
    def test_sequence(self):
        self.assertEqual(solve("1347"), 7)
        self.assertEqual(solve("1357"), 10)
        self.assertEqual(solve("13471"), 12)
        self.assertEqual(solve("134721"), 13)
        self.assertEqual(solve("1347231"), 20)
        self.assertEqual(solve("13472315"), 28)
