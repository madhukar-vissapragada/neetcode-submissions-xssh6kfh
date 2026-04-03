class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) > 1:
            return max(self.solve(nums[0:len(nums)-1], 0, {}), 
                    self.solve(nums[1:len(nums)], 0, {})) 
        return nums[0]
    

    def solve(self, nums: List[int], current_house: int, memo: dict) -> int:
        if current_house >= len(nums):
            return 0 
        
        if current_house in memo:
            return memo[current_house]
        
        rob = nums[current_house] + self.solve(nums, current_house + 2, memo)
        do_not_rob = self.solve(nums, current_house + 1, memo)

        result = max(rob, do_not_rob)
        memo[current_house] = result
        return result
         