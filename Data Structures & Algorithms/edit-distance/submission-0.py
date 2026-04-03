class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.solve(word1, word2, 0, 0, {})

    def solve(self, word1, word2, i, j, memo):
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        current_key = (i, j)
        if current_key in memo:
            return memo[current_key]

        if word1[i] == word2[j]:
            return self.solve(word1, word2, i+1, j+1, memo)

        insert = 1 + self.solve(word1, word2, i, j+1, memo)
        delete = 1 + self.solve(word1, word2, i+1, j, memo)
        replace = 1 + self.solve(word1, word2, i+1, j+1, memo)

        result = min(insert, delete, replace)
        memo[current_key] = result 
        return result 