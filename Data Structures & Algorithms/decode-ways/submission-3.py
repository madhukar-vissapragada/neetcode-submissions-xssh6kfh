class Solution:
    def numDecodings(self, s: str) -> int:
        return self.solve(s, 0, {})

    def solve(self, s: str, current_index: int, memo: dict) -> int:
        if current_index == len(s):
            return 1

        if s[current_index] == "0":
            return 0  
        
        if current_index in memo:
            return memo[current_index]
        
        one_ele = two_ele = 0
        if 1 <= int(s[current_index:current_index + 1]) < 10:
            one_ele = self.solve(s, current_index + 1, memo)
        if 10 <= int(s[current_index:current_index + 2]) <= 26:
            two_ele = self.solve(s, current_index + 2, memo)
        
        result = one_ele + two_ele
        memo[current_index] = result
        return result 
        