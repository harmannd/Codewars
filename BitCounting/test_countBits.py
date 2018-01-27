from unittest import TestCase
from bit_counting import countBits

class TestCountBits(TestCase):
    def test_countBits(self):
        self.assertEqual(countBits(0), 0);
        self.assertEqual(countBits(4), 1);
        self.assertEqual(countBits(7), 3);
        self.assertEqual(countBits(9), 2);
        self.assertEqual(countBits(10), 2);
