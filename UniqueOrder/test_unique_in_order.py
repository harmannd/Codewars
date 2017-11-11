from unittest import TestCase
from unique_order import unique_in_order

class TestUnique_in_order(TestCase):
    def test_unique_in_order(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
    def test_boundary(self):
        self.assertEqual(unique_in_order(''), [])
    def test_single_rep(self):
        self.assertEqual(unique_in_order('aaa'), ['a'])
