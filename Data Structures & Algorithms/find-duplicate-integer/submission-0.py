class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map = {}
        result = None

        for current in nums:
            if current in hash_map:
                hash_map[current] += 1 
            else:
                hash_map[current] = 1 
        
        for key, value in hash_map.items():
            if value > 1:
                result = key 
                break
        
        return result 
        
    
        

        
        
        