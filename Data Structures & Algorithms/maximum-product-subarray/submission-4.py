class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return self.solve(nums, 0) 
    

    def solve(self, nums: List[int], start: int) -> int:
        if start == len(nums):
            return -100
        
        max_result = -100
        result = 1
        for index in range(start, len(nums)):
            result = result * nums[index]
            if result > max_result:
                max_result = result

        return max(max_result, self.solve(nums, start + 1))
   