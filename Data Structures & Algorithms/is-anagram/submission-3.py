class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}

        if len(s) < len(t):
            return False

        for current in s:
            if current in map_s:
                map_s[current] += 1
            else:
                map_s[current] = 1

        for current in t:
            if current in map_s:
                map_s[current] -= 1
                if map_s[current] == 0:
                    del map_s[current]
        
        if len(map_s) == 0:
            return True 
        
        return False
        
        

        