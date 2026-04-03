class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        max_length = 0 
        i = j = 0 

        while j < len(s):
            if s[j] in freq:
                freq.discard(s[i])
                i += 1
            else:
                freq.add(s[j])
                max_length = max(max_length, j - i + 1)
                j += 1

        return max_length


