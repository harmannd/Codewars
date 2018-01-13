from unittest import TestCase
from integer_depth import compute_depth

class TestCompute_depth(TestCase):
    def test_compute_depth(self):
        self.assertEqual(compute_depth(1), 10)
        self.assertEqual(compute_depth(42), 9)
