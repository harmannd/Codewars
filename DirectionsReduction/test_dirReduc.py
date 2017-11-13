from unittest import TestCase
from direction_reduction import dirReduc

class TestDirReduc(TestCase):
    def test_remove(self):
        self.assertEqual(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ['WEST'])
    def test_no_remove(self):
        self.assertEqual(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]), ["NORTH", "WEST", "SOUTH", "EAST"])