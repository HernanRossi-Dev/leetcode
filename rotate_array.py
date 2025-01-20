from typing import Callable, List

class SolutionComplex:
    _pointer_1: int = 0
    _pointer_2: int = 0
    _nums: List[int] = list()

    @property
    def pointer_1(self) -> int:
        return self._pointer_1

    @property
    def pointer_2(self) -> int:
        return self._pointer_2

    def set_pointer_1(self, value: int) -> None:
        self._pointer_1 = value

    def set_pointer_2(self, value: int) -> None:
        self._pointer_2 = value

    def increment_pointers(self) -> None:
        print('Incrementing Pointers')
        self._pointer_1 += 1
        self._pointer_2 += 1

    def converge_pointers(self) -> None:
        print('Converging Pointers')
        self._pointer_1 += 1
        self._pointer_2 -= 1

    def increment_one(self) -> None:
        print('Increment Pointer 1')
        self._pointer_1 += 1

    def do_swaps(self, alter_pointer_fun: Callable) -> None:
        print(f"Swapping locations {self.pointer_1} <-> {self.pointer_2}")
        temp = self._nums[self.pointer_1]
        self._nums[self.pointer_1] = self._nums[self.pointer_2]
        self._nums[self.pointer_2] = temp
        alter_pointer_fun()
        print(f'Completed swap: {self._nums}')

    def rotate(self, nums: List[int], k: int) -> None:
        """Do not return anything, modify nums in-place instead."""
        self._nums = nums
        self.set_pointer_1(0)
        self.set_pointer_2(k)
        if k >= len(nums):
            k = k - len(nums)
            if not k:
                return
        if len(nums) < 2:
            return
        if len(nums) == 2:
            self.set_pointer_2(1)
            if k % 2 == 1:
                self.do_swaps(self.increment_pointers)
            return
        # # Pass One Middle
        self.set_pointer_1(0)
        self.set_pointer_2(k)
        while self.pointer_1 < k and self.pointer_2 < len(nums):
            self.do_swaps(self.increment_pointers)
        # Pass two End
        self.set_pointer_1(0)
        self.set_pointer_2(k + k)
        while self.pointer_2 < len(nums):
            self.do_swaps(self.increment_pointers)

        # Pass three Start
        self.set_pointer_1(0)
        self.set_pointer_2(k - 1)
        while self.pointer_1 < self.pointer_2:
            self.do_swaps(self.converge_pointers)
            if self.pointer_1 >= self.pointer_2:
                left = nums[self.pointer_1 - 1]
                right = nums[self.pointer_2 + 1]
                mid = nums[self.pointer_1]
                if left > mid:
                    nums[self.pointer_1 - 1] = mid
                    nums[self.pointer_1] = left
                elif mid > right:
                    nums[self.pointer_1 + 1] = mid
                    nums[self.pointer_1] = right
                return

class SolutionSimple:
    _pointer: int = 0
    _nums: List[int] = list()

    @property
    def pointer(self) -> int:
        return self._pointer

    def set_pointer(self, value: int) -> None:
        self._pointer = value
        if self._pointer >= len(self._nums):
            self._pointer = value - len(self._nums)

    def do_swaps(self, n: int, m: int) -> None:
        print(f"Swapping locations {n} <-> {m}")
        temp = self._nums[n]
        self._nums[n] = self._nums[m]
        self._nums[m] = temp

    def rotate(self, nums: List[int], k: int) -> None:
        """Do not return anything, modify nums in-place instead."""
        if len(nums) < 2:
            return
        if k > len(nums):
            k = k - len(nums)
        self._nums = nums
        self.set_pointer(0)
        current_item = start = self._nums[self.pointer]
        # print(f'Starting state: {current_item} {start}: {k=} {len(nums)}')

        for _ in nums:
            # set pointer to target
            self.set_pointer(self.pointer + k)
            next_item = self._nums[self.pointer]
            print(f'Moving current: {current_item} to location: {self.pointer}, picking up next: {next_item}')
            self._nums[self.pointer] = current_item
            current_item = next_item
            if next_item == start:
                self.set_pointer(self.pointer + 1)
                current_item = self._nums[self.pointer]
                start = current_item



def main():
    nums = [1, 2, 3]
    k = 1
    # test = SolutionComplex()
    test = SolutionSimple()
    test.rotate(nums, k)


if __name__ == '__main__':
    main()
