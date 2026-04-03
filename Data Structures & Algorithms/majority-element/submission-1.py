class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None 
        count = 0 

        for current in nums:
            if count == 0:
                element = current 
            
            if element == current:
                count += 1 
            else:
                count -= 1 
        
        return element 
            


            
        