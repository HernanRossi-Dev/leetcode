import unittest
from typing import List

MATCHING = {'(': ')', '{': '}', '[': ']'}


class MatchingParentheses:

    @staticmethod
    def is_valid(s: str) -> bool:
        if len(s) < 2:
            return False
        stack: List[str] = []
        split: List[str] = list(s)
        for idx, paren in enumerate(split):
            if paren in MATCHING.keys():
                stack.append(paren)
            elif not stack:
                return False
            elif paren == MATCHING[stack[-1]]:
                stack.pop(-1)
            else:
                return False
        if not stack:
            return True
        return False


class TestSummaryRanges(unittest.TestCase):
    def setUp(self):
        self.matching_paren = MatchingParentheses()

    def test_true_case(self):
        test = "([])"
        result = self.matching_paren.is_valid(test)
        self.assertEqual(result, True)

    def test_false_case(self):
        test = "(]"
        result = self.matching_paren.is_valid(test)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
