class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for current in nums:
            if current in freq:
                freq[current] += 1 
            else:
                freq[current] = 1 
        
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        result = []
        count = 0
        for key, value in freq.items():
            result.append(key)
            count += 1 
            if count == k:
                break
    
        return result 

        