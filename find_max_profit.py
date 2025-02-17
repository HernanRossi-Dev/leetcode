from typing import List
import unittest


class MaxProfit:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        total_profit = 0
        current_min = prices[0]
        max_profit = 0
        for p in prices:
            current_profit = p - current_min
            if current_profit > max_profit:
                max_profit = 0
                current_min = p
                total_profit = total_profit + current_profit
            if p < current_min:
                current_min = p
        return total_profit


class TestSummaryRanges(unittest.TestCase):
    def setUp(self):
        self.find_max_profit = MaxProfit()

    def test_case_one(self):
        test = [7, 1, 5, 3, 6, 4]
        result = self.find_max_profit.maxProfit(test)
        self.assertEqual(result, 7)

    def test_case_two(self):
        test = [1, 2, 3, 4, 5]
        result = self.find_max_profit.maxProfit(test)
        self.assertEqual(result, 4)

    def test_case_three(self):
        test = [7, 6, 4, 3, 1]
        result = self.find_max_profit.maxProfit(test)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
