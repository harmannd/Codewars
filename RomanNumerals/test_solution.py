from unittest import TestCase
from roman_numerals import solution

class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(solution(1), 'I', "solution(1),'I'")
        self.assertEqual(solution(4), 'IV', "solution(4),'IV'")
        self.assertEqual(solution(6), 'VI', "solution(6),'VI'")
        self.assertEqual(solution(9), 'IX', "solution(9), 'IX'")
        self.assertEqual(solution(89), 'LXXXIX', "solution(89), 'LXXXIX'")
        self.assertEqual(solution(91), 'XCI')
        self.assertEqual(solution(400), 'CD')
        self.assertEqual(solution(900), 'CM')
