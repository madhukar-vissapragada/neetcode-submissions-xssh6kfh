from functools import reduce 
from operator import xor 

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = []
        self.solve(nums, 0, [], result)

        ans = 0
        for current in result:
            ans += reduce(xor, current, 0)
        
        return ans 

    def solve(self, nums, current_index, current_subset, result):
        if current_index == len(nums):
            result.append(current_subset.copy())
            return 

        current_subset.append(nums[current_index])
        self.solve(nums, current_index + 1, current_subset, result)       
        current_subset.pop()
        self.solve(nums, current_index + 1, current_subset, result)
        