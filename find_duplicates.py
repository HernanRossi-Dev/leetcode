from typing import Dict, List


class Solution:

    @staticmethod
    def has_duplicate(nums: List[int]) -> bool:
        map: Dict[int, int] = dict()
        for n in nums:
            if map.get(n):
                return True
            else:
                map[n] = 1
        return False


def main():
    nums = [1, 2, 3, 3]
    result = Solution.has_duplicate(nums)
    print(f'{result=}')


if __name__ == '__main__':
    main()