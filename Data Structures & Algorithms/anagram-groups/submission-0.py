class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for current in strs:
            item = []
            key = tuple(sorted(current))

            if key in freq:
                freq[key].append(current)
            else:
                freq[key] = []
                freq[key].append(current)
        
        return list(freq.values())

            
        