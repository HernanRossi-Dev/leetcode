from typing import List


class Solution:

    def remove_duplicates(self, nums: List[int]) -> int:
        pointer = 0
        max_dup = False
        previous = None
        for i in nums:
            current = i
            if current == previous:
                if not max_dup:
                    max_dup = True
                    nums[pointer] = current
                    pointer += 1
                else:
                    print(f"Maximum Duplicates saved to list for value {current}")
            else:
                nums[pointer] = current
                pointer += 1
                max_dup = False
            previous = current
        return pointer


def main():
    values = [1, 1, 1, 2, 2, 3]
    test = Solution()
    result = test.remove_duplicates(values)
    print(f"Final result {result=}")


if __name__ == "__main__":
    main()
