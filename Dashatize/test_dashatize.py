from unittest import TestCase
from dashatize import dashatize

class TestDashatize(TestCase):
    def test_dashatize_normal(self):
        self.assertEqual(dashatize(274), "2-7-4", "Should return 2-7-4")
        self.assertEqual(dashatize(5311),"5-3-1-1", "Should return 5-3-1-1")
        self.assertEqual(dashatize(86320),"86-3-20", "Should return 86-3-20")
        self.assertEqual(dashatize(974302),"9-7-4-3-02", "Should return 9-7-4-3-02")

    def test_dashatize_wierd(self):
        self.assertEqual(dashatize(None), "None", "Should return None")
        self.assertEqual(dashatize(0), "0", "Should return 0")
        self.assertEqual(dashatize(-1), "1", "Should return 1")
        self.assertEqual(dashatize(-28369), "28-3-6-9", "Should return 28-3-6-9")
