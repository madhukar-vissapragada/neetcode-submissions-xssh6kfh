class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = 0

        for current in nums:
            total_sum += current

        if total_sum % 2 == 0:
            target_sum = total_sum // 2
            dp = [[-1 for j in range(0, target_sum+1)] for i in range(len(nums))]
            return self.solve(nums, target_sum, 0, dp)

        return False

    def solve(self, nums: List[int], target_sum: int, current_index: int, memo):
        if target_sum == 0:
            return True

        if current_index == len(nums):
            return False

        if memo[current_index][target_sum] != -1:
            return memo[current_index][target_sum]

        pick = 0
        if target_sum - nums[current_index] >= 0:
            pick = self.solve(nums, target_sum - nums[current_index], current_index + 1, memo)
        not_to_pick = self.solve(nums, target_sum, current_index + 1, memo)

        result = pick or not_to_pick

        memo[current_index][target_sum] = result
        return result
