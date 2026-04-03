class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        result = None

        for index, value in enumerate(nums):
            find = target - value 

            if find in freq:
                find_index = freq[find]
                if index < find_index:
                    result = [index, find_index]
                else:
                    result = [find_index, index]
                break
            else:
                freq[value] = index
        
        return result
        