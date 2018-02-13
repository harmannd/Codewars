from unittest import TestCase
from highest_scoring_word import high

class TestHigh(TestCase):
    def test_high(self):
        self.assertEqual(high('man i need a taxi up to ubud'), 'taxi')
        self.assertEqual(high('what time are we climbing up the volcano'), 'volcano')
        self.assertEqual(high('take me to semynak'), 'semynak')
