from typing import List

class Solution:
    _pointer_1: int = 0
    _pointer_2: int = 0
    _nums: List[int] = list()

    @property
    def pointer_1(self) -> int:
        return self._pointer_1

    @property
    def pointer_2(self) -> int:
        return self._pointer_2

    @property
    def increment_pointer_1(self) -> None:
        self._pointer_1 += 1
        if self._pointer_1 == len(self._nums):
            self._pointer_1 = 0

    @property
    def increment_pointer_2(self) -> None:
        self._pointer_2 += 1
        if self._pointer_2 == len(self._nums):
            self._pointer_2 = 0

    def set_pointer_1(self, value: int) -> None:
        self._pointer_1 = value

    def set_pointer_2(self, value: int) -> None:
        value = value if value < len(self._nums) - 1 else len(self._nums) - 1
        self._pointer_2 = value

    def do_swaps(self) -> None:
        print(f"Swapping locations {self.pointer_1} <-> {self.pointer_2}")
        temp = self._nums[self.pointer_1]
        self._nums[self.pointer_1] = self._nums[self.pointer_2]
        self._nums[self.pointer_2] = temp
        self.increment_pointer_1
        self.increment_pointer_2
        print(f'Completed swap: {self._nums}')

    def rotate(self, nums: List[int], k: int) -> None:
        """Do not return anything, modify nums in-place instead."""
        self._nums = nums
        self.set_pointer_1(0)
        if len(nums) < 2:
            return
        self.set_pointer_2(1)
        if len(nums) == 2:
            if k % 2 == 1:
                self.do_swaps()
            return
        self.set_pointer_2(k)
        while self.pointer_1 < k:
            self.do_swaps()
        self.set_pointer_1(0)
        while self.pointer_1 < k:
            self.do_swaps()

def main():
    nums = [1, 2, 3]
    k = 1
    test = Solution()
    test.rotate(nums, k)


if __name__ == '__main__':
    main()