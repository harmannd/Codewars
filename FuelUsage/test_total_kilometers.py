from unittest import TestCase
from fuel_usage import total_kilometers, check_distance

class TestTotal_kilometers(TestCase):
    def test_total_kilometers(self):
        self.assertEqual(total_kilometers(9.3, 87.3), 938.71)
        self.assertEqual(total_kilometers(11.7, 63.4), 541.88)
        self.assertEqual(total_kilometers(16,73), 456.25)

    def test_check_distance(self):
        self.assertEqual(check_distance(700, 10, 60), "You will need to refuel")
        self.assertEqual(check_distance(467, 12.3, 60), [[0, 467, 60], [100, 367, 47.7], [200, 267, 35.40], [300, 167, 23.10], [400, 67, 10.80]])
