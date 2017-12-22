from unittest import TestCase
from permutations import ssc_forperm

class TestSsc_forperm(TestCase):
    def test_ssc_forperm(self):
        self.assertEqual(ssc_forperm([6, 12, -1]), [{"total perm": 6}, {"total ssc": 204}, {"max ssc": 47}, {"min ssc": 21}])
