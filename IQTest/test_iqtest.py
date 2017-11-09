from unittest import TestCase
from iqtest import iq_test

class TestIQTest(TestCase):
    def test_odd(self):
        self.assertEqual(iq_test("1 2 2"), 1, "First number different")
    def test_even(self):
        self.assertEqual(iq_test("2 1 1"), 1, "First number different")