class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.solve(nums, 0, -1)
    
    def solve(self, nums: List[int], current_index: int, prev_index: int) -> int:
        if current_index == len(nums):
            return 0
        
        include = not_include = 0 

        if prev_index == -1 or nums[prev_index] < nums[current_index]:
            include = 1 + self.solve(nums, current_index + 1, prev_index=current_index)
        not_include = self.solve(nums, current_index + 1, prev_index)

        result = max(include, not_include)
        return result
