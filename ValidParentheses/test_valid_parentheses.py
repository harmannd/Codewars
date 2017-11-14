from unittest import TestCase
from valid_parens import valid_parentheses

class TestValid_parentheses(TestCase):
    def test_valid_parentheses(self):
        self.assertEqual(valid_parentheses("  ("), False)
        self.assertEqual(valid_parentheses(")test"), False)
        self.assertEqual(valid_parentheses(""), True)
        self.assertEqual(valid_parentheses("hi())("), False)
        self.assertEqual(valid_parentheses("hi(hi)()"), True)
