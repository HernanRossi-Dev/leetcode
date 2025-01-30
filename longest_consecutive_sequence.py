from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ConsecutiveSet:
    set_upper: int # This is the upper bound on the current consecutive set that contains the number
    set_lower: int # This is the lower bound on the current consecutive set that contains the number

class Solution:
    def extend_sequences(self, set_one: ConsecutiveSet, set_two: ConsecutiveSet):
        set_one.set_upper = set_two.set_upper if set_two.set_upper > set_one.set_upper else set_one.set_upper
        set_one.set_lower = set_two.set_lower if set_two.set_lower < set_one.set_lower else set_one.set_lower
        set_two.set_upper = set_one.set_upper if set_one.set_upper > set_two.set_upper else set_two.set_upper
        set_two.set_lower = set_one.set_lower if set_one.set_lower < set_two.set_lower else set_two.set_lower

    def check_if_consecutive(self, num: int, seq_map: Dict[int, ConsecutiveSet]) -> None:
        current_obj = seq_map[num]
        if item := seq_map.get(current_obj.set_lower - 1):
            self.extend_sequences(current_obj, item)
        if item := seq_map.get(current_obj.set_upper + 1):
            self.extend_sequences(current_obj, item)
        if item := seq_map.get(current_obj.set_lower - 1):
            self.extend_sequences(current_obj, item)
        if item := seq_map.get(current_obj.set_upper + 1):
            self.extend_sequences(current_obj, item)

    def longestConsecutive(self, nums: List[int]) -> int:
        seq_map: Dict[int, ConsecutiveSet] = { num: ConsecutiveSet(set_lower=num, set_upper=num) for num in nums}
        if len(nums) < 2:
            return len(nums)
        for _ in range(1):
            for num in nums:
                self.check_if_consecutive(num, seq_map)
        length_list = [item.set_upper - item.set_lower + 1 for item in seq_map.values()]
        max_len = max(length_list)
        return max_len

def main():
    nums = [-4,-1,4,-5,1,-6,9,-6,0,2,2,7,0,9,-3,8,9,-2,-6,5,0,3,4,-2]
    result = Solution().longest_consecutive(nums)
    print(f'Result = {result}')


if __name__ == "__main__":
    main()
