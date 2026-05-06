class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        self.solve(nums, 0, [], result)
        return list(result) 
    

    def solve(self, nums, current_index, current_subset, result):
        if current_index == len(nums):
            result.add(tuple(current_subset.copy()))
            return 
        
        current_subset.append(nums[current_index])
        self.solve(nums, current_index + 1, current_subset, result)
        current_subset.pop()
        self.solve(nums, current_index + 1, current_subset, result)

            