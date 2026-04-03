class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for current in strs:
            arr = [0] * 26
            for ch in current:
                index = ord(ch) - ord('a')
                arr[index] += 1 
            
            key = tuple(arr)
            if key in freq:
                freq[key].append(current)
            else:
                freq[key] = []
                freq[key].append(current)
        
        return list(freq.values())

            
        