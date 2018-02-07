from unittest import TestCase
from simple_string import solve

class TestSolve(TestCase):
    def test_solve(self):
        self.assertEqual(solve("3(ab)"), "ababab")
        self.assertEqual(solve("2(a3(b))"), "abbbabbb")
        self.assertEqual(solve("3(b(2(c)))"), "bccbccbcc")
        self.assertEqual(solve("k(a3(b(a2(c))))"), "kabaccbaccbacc")
