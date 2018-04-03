from unittest import TestCase
from upside_down import solve

class TestSolve(TestCase):
    def test_solve(self):
        self.assertEqual(solve(0, 10), 3)
        self.assertEqual(solve(10, 100), 4)
        self.assertEqual(solve(100, 1000), 12)
        self.assertEqual(solve(1000, 10000), 20)
        self.assertEqual(solve(10000, 15000), 6)
        self.assertEqual(solve(15000, 20000), 9)
        self.assertEqual(solve(60000, 70000), 15)
        self.assertEqual(solve(60000, 130000), 55)
