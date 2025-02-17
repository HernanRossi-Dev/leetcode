import unittest
from typing import List


class Solution:

    def print_entry(self, current: int, current_min: int, result: List[str]) -> None:
        if current == current_min:
            result.append(f"{current}")
        else:
            result.append(f"{current_min}->{current}")

    def summary_ranges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        current_min = current = nums[0]
        result: List[str] = []
        for n in nums[1:]:
            if n == current + 1:
                current = n
                continue
            self.print_entry(current, current_min, result)
            current_min = current = n
        self.print_entry(current, current_min, result)
        return result


class TestSummaryRanges(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_odd_number(self):
        test = [0, 1, 2, 4, 5, 7]
        result = self.solution.summary_ranges(test)
        self.assertEqual(result, ["0->2", "4->5", "7"])

    def test_even_number(self):
        test = [0, 1, 2, 4, 5, 7, 8]
        result = self.solution.summary_ranges(test)
        self.assertEqual(result, ["0->2", "4->5", "7->8"])


if __name__ == "__main__":
    unittest.main()
