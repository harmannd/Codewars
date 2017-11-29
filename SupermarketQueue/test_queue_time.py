from unittest import TestCase
from supermarket_queue import queue_time

class TestQueue_time(TestCase):
    def test_empty_queue(self):
        self.assertEqual(queue_time([], 1), 0, "wrong answer for case with an empty queue")
    def test_single_person(self):
        self.assertEqual(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
        self.assertEqual(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
    def test_multiple(self):
        self.assertEqual(queue_time([1, 2, 3, 4, 5], 1), 15, "wrong answer for a single till")
        self.assertEqual(queue_time([1, 2, 3, 4, 5], 100), 5, "wrong answer for a case with a large number of tills")
        self.assertEqual(queue_time([2, 2, 3, 3, 4, 4], 2), 9, "wrong answer for a case with two tills")
    def test_random(self):
        self.assertEqual(queue_time([2, 3, 10], 2), 12)
        self.assertEqual(queue_time([6, 14, 8, 45, 18, 14, 22, 45, 5, 34, 26, 14, 47, 26, 32, 17], 5), 91)