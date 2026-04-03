class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        result = None

        for current in nums:
            if current in freq:
                freq[current] += 1 
            else:
                freq[current] = 1 
        
        for key, value in freq.items():
            if value > len(nums)//2:
                result = key
                break
        
        return result
            


            
        