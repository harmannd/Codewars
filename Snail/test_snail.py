from unittest import TestCase
from snail_path import snail

class TestSnail(TestCase):
    def test_snail1(self):
        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(snail(array), expected)

    def test_snail2(self):
        array = [[1, 2, 3],
                 [8, 9, 4],
                 [7, 6, 5]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(snail(array), expected)

