from typing import Dict, List


class Solution:

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        map: Dict[int, int] = dict()

        for index, num in enumerate(nums):
            map[num] = index

        for idx_1, num in enumerate(nums):
            sub = target - num
            if idx_2 := map.get(sub):
                if idx_1 != idx_2:
                    return [idx_1, idx_2]


def main():
    nums = [3, 4, 5, 6]
    target = 7
    result = Solution.twoSum(nums, target)


if __name__ == "__main__":
    main()