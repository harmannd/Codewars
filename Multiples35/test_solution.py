from unittest import TestCase
from multiples import solution

class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(solution(10), 23)
        self.assertEqual(solution(1), 0)
