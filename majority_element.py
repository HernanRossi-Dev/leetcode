import math
from typing import List


class Solution:
    def majority_element_brute_force(self, nums: List[int]) -> int:
        unique_counts = {}
        for item in nums:
            if value := unique_counts.get(item):
                unique_counts[item] = value + 1
            else:
                unique_counts[item] = 1
        max_count = 0
        max_key = None
        for key, value in unique_counts.items():
            if value > max_count:
                max_count = value
                max_key = key
        return max_key

    def majority_element_optimized(self, nums: List[int]) -> int:
        """This is solvable using the Boyer-Moore Majority Algorithm"""
        value = None
        counter = 0
        for item in nums:
            if not counter:
                value = item
                counter = 1
            elif item == value:
                counter += 1
            else:
                counter -= 1
        return value


def main():
    test_runner = Solution()
    test_values = [2, 2, 1, 1, 1, 2, 2]
    test_runner.majority_element_optimized(test_values)


if __name__ == "__main__":
    main()
