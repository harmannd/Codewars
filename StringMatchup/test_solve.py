from unittest import TestCase
from string_matchup import solve

class TestSolve(TestCase):
    def test_solve(self):
        self.assertEqual(solve(['abc', 'abc', 'xyz', 'abcd', 'cde'], ['abc', 'cde', 'uap']), [2, 1, 0])
        self.assertEqual(solve(['abc', 'xyz', 'abc', 'xyz', 'cde'], ['abc', 'cde', 'xyz']), [2, 1, 2])
        self.assertEqual(solve(['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']), [2, 0, 1])
