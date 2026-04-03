class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.solve(0, 0, s, t, {})
    
    def solve(self, i: int, j: int, s: str, t: str, memo: dict) -> int:
        if j == len(t):
            return 1 
        if i == len(s):
            return 0 
        
        current_key = (i, j)
        if current_key in memo:
            return memo[current_key]

        equal = not_equal = 0
        if s[i] == t[j]:
            equal = self.solve(i+1, j+1, s, t, memo) + self.solve(i+1, j, s, t, memo)
        else:
            not_equal = self.solve(i+1, j, s, t, memo)

        result = equal + not_equal 
        memo[current_key] = result 

        return result 

        