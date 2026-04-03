class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) == len(s3):
            return self.solve(s1, s2, s3, 0, 0, 0, {})
        return False
    
    def solve(self, s1: str, s2: str, s3: str, i: int, j: int, k: int, memo: dict) -> bool:
        if k == len(s3): 
            return True 
        

        current_key = (i, j, k)
        if current_key in memo:
            return memo[current_key]
        
        check_a = False
        if (i < len(s1) and s1[i] == s3[k]) and (j < len(s2) and s2[j] == s3[k]):
            possible_a = self.solve(s1, s2, s3, i+1, j, k+1, memo)
            possible_b = self.solve(s1, s2, s3, i, j+1, k+1, memo)

            check_a = possible_a or possible_b
        
        check_b = check_c = False
        if i < len(s1) and s1[i] == s3[k]:
            check_b = self.solve(s1, s2, s3, i+1, j, k+1, memo)
        if j < len(s2) and s2[j] == s3[k]:
            check_c = self.solve(s1, s2, s3, i, j+1, k+1, memo)

        result = check_a or check_b or check_c
        memo[current_key] = result
        return result 
        