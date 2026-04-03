class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1 
        suffix = 1 
        max_product = -float('inf') 

        for index in range(len(nums)):
            prefix *= nums[index]
            suffix *= nums[len(nums)-1-index]

            max_product = max(max_product, prefix, suffix)
            if prefix == 0:
                prefix = 1 
            if suffix == 0:
                suffix = 1 
        return max_product
        