class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.solve(s, 0, len(s) - 1, {})

    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def solve(self, s: str, left: int, right: int, memo: dict) -> str:
        if left > right:
            return ""

        if self.is_palindrome(s, left, right):
            return s[left:right + 1]
        
        current_key = (left, right)
        if current_key in memo:
            return memo[current_key]

        a = self.solve(s, left + 1, right, memo)
        b = self.solve(s, left, right - 1, memo)

        result =  a if len(a) > len(b) else b
        memo[current_key] = result 
        return result 
