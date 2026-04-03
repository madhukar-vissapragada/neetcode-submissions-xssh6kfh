class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        list_sum = sum(nums)
        return self.solve(nums, 0, target, {})

    def solve(self, nums: List[int], current_index: int, target: int, memo) -> int:
        if current_index == len(nums):
            return 1 if target == 0 else 0

        current_key = (current_index, target)
        if current_key in memo:
            return memo[current_key]

        plus = minus = 0
        plus += self.solve(nums, current_index + 1, target - nums[current_index], memo)
        minus += self.solve(nums, current_index + 1, target + nums[current_index], memo)
        result = plus + minus
        memo[current_key] = result

        return result
