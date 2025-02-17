import unittest
from operator import itemgetter
from typing import List


class MergeIntervals:

    @staticmethod
    def merge(intervals: List[List[int]]) -> List[List[int]]:
        result_intervals = []
        sort_list = sorted(intervals, key=itemgetter(0))
        interval = sort_list.pop(0)
        int_start = interval[0]
        int_end = interval[1]
        """go through all the items in the interval and if the starting number of an interval is within
        the current interval make this ending number"""
        while len(sort_list):
            interval = sort_list.pop(0)
            if int_start <= interval[0] <= int_end:
                int_end = interval[1] if interval[1] > int_end else int_end
            else:
                result_intervals.append([int_start, int_end])
                int_start = interval[0]
                int_end = interval[1]
        result_intervals.append([int_start, int_end])
        return result_intervals


class TestSummaryRanges(unittest.TestCase):
    def setUp(self):
        self.merge_intervals = MergeIntervals()

    def test_two_intervals(self):
        test = [[1, 4], [0, 4]]
        result = self.merge_intervals.merge(test)
        self.assertEqual(result, [[0, 4]])

    def test_five_intervals(self):
        test = [[1, 3], [2, 6], [8, 10], [15, 18]]
        result = self.merge_intervals.merge(test)
        self.assertEqual(result, [[1, 6], [8, 10], [15, 18]])


if __name__ == "__main__":
    unittest.main()
