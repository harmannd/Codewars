from unittest import TestCase
from piglatin import pig_it

class TestPig_it(TestCase):
    def test_pig_it(self):
        self.assertEqual(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
        self.assertEqual(pig_it('This is my string'), 'hisTay siay ymay tringsay')
