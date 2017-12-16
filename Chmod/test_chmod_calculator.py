from unittest import TestCase
from chmod import chmod_calculator

class TestChmod_calculator(TestCase):
    def test_chmod_calculator(self):
        self.assertEqual(chmod_calculator({"user": 'rwx', "group": 'r-x', "other": 'r-x'}), "755")
        self.assertEqual(chmod_calculator({"user": 'rwx', "group": 'r--', "other": 'r--'}), "744")
        self.assertEqual(chmod_calculator({"user": 'r-x', "group": 'r-x', "other": '---'}), "550")
        self.assertEqual(chmod_calculator({"group": 'rwx'}), "070")
        self.assertEqual(chmod_calculator({}), "000")
