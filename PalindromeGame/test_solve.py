from unittest import TestCase
from palindrome_game import solve

class TestSolve(TestCase):
    def test_solve1(self):
        self.assertEqual(solve('abc', 'xyz'), 2)

    def test_solve2(self):
        self.assertEqual(solve('abc', 'axy'), 2)

    def test_solve3(self):
        self.assertEqual(solve('abc', 'bax'), 2)

    def test_solve4(self):
        self.assertEqual(solve('btzgd', 'svjyb'), 2)

    def test_solve5(self):
        self.assertEqual(solve('eyfjy', 'ooigv'), 1)

    def test_solve6(self):
        self.assertEqual(solve('mctimp', 'eyqbnh'), 1)

    def test_solve7(self):
        self.assertEqual(solve('qtkxttl', 'utvohqk'), 2)
