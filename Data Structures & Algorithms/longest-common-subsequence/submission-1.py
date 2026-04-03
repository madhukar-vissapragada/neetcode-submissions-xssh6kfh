class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.solve(text1, text2, 0, 0, {})
    

    def solve(self, text1: str, text2: str, i: int, j: int, memo: dict) -> int:
        if i == len(text1) or j == len(text2):
            return 0 

        current_key = (i, j)
        if current_key in memo:
            return memo[current_key]

        equal = not_equal = 0
        if text1[i] == text2[j]:
            equal = 1 + self.solve(text1, text2, i + 1, j + 1, memo)
        if text1[i] != text2[j]:
            not_equal = max(self.solve(text1, text2, i+1, j, memo), self.solve(text1, text2, i, j+1, memo))

        result = equal + not_equal 
        memo[current_key] = result
        return result 


        