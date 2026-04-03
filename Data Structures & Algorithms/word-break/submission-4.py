class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        return self.solve(s, set(wordDict), 0, memo)
    

    def solve(self, s: str, word_dict: set, start: int, memo: dict) -> bool:
        
        if start == len(s):
            return True
        
        # 🔹 Memo check
        if start in memo:
            return memo[start]
        
        for index in range(start, len(s)):
            if s[start:index+1] in word_dict:
                if self.solve(s, word_dict, index + 1, memo):
                    memo[start] = True
                    return True
        
        memo[start] = False
        return False