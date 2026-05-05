class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
       return self.solve(nums, 0, 0) 

    def solve(self, nums, current_index, current_xor):
        if current_index == len(nums):
            return current_xor
 
        include = self.solve(nums, current_index + 1, current_xor ^ nums[current_index])       
        exclude = self.solve(nums, current_index + 1, current_xor)

        return include + exclude 
