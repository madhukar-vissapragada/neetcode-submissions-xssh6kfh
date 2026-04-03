class Solution:
    def __init__(self):
        self.is_pal = {}
        self.max_length = 0
        self.longest_string = ""

    def longestPalindrome(self, s: str) -> str:
        self.solve(s, 0)
        return self.longest_string

    def solve(self, s: str, start: int) -> None:

        def is_palindrome(s: str, start: int, end: int) -> bool:
            if start >= end:
                return True

            if (start, end) in self.is_pal:
                return self.is_pal[(start, end)]

            if s[start] != s[end]:
                self.is_pal[(start, end)] = False
            else:
                self.is_pal[(start, end)] = is_palindrome(s, start + 1, end - 1)

            return self.is_pal[(start, end)]
        
        if start == len(s):
            return 

        for index in range(start, len(s)):
            if is_palindrome(s, start, index):
                length = index - start + 1
                if length > self.max_length:
                    self.max_length = length
                    self.longest_string = s[start:index+1]

        self.solve(s, start+1)


                



