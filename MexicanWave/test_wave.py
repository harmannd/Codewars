from unittest import TestCase
from mexican_wave import wave

class TestWave(TestCase):
    def test_wave(self):
        self.assertEqual(wave("hello"), ["Hello", "hEllo", "heLlo", "helLo", "hellO"])
        self.assertEqual(wave(""), [])
        self.assertEqual(wave("two words"), ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"])
        self.assertEqual(wave(" gap "), [" Gap ", " gAp ", " gaP "])