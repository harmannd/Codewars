from unittest import TestCase
from countsmileyfaces import count_smileys

class TestCount_smileys(TestCase):
    def test_count_smileys(self):
        self.assertEqual(count_smileys([]), 0)
        self.assertEqual(count_smileys([':D', ':~)', ';~D', ':)']), 4)
        self.assertEqual(count_smileys([':)', ':(', ':D', ':O', ':;']), 2)
        self.assertEqual(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)