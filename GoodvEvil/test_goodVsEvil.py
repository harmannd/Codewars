from unittest import TestCase
from goodVsEvil import goodVsEvil

class TestGoodVsEvil(TestCase):
    def test_goodVsEvil(self):
        self.assertEqual
        (
            goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'),
            'Battle Result: Evil eradicates all trace of Good',
            'Evil should win'
        )

    def test_goodVsEvil(self):
        self.assertEqual
        (
            goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0'),
            'Battle Result: Good triumphs over Evil',
            'Good should win'
        )

    def test_goodVsEvil(self):
        self.assertEqual
        (
            goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'),
            'Battle Result: No victor on this battle field',
            'Should be a tie'
        )