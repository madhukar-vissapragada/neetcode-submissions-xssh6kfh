class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.solve(nums, 0, -1, {})
    
    def solve(self, nums: List[int], current_index: int, prev_index: int, memo: dict) -> int:
        if current_index == len(nums):
            return 0
        
        current_key = (current_index, prev_index)
        if current_key in memo:
            return memo[current_key]
        
        include = not_include = 0 

        if prev_index == -1 or nums[prev_index] < nums[current_index]:
            include = 1 + self.solve(nums, current_index + 1, current_index, memo)
        not_include = self.solve(nums, current_index + 1, prev_index, memo)

        result = max(include, not_include)
        memo[current_key] = result
        return result
