class Solution:
    def climbStairs(self, n: int) -> int:
        return self.solve(n, 0, {}) 
    
    def solve(self, n: int, current_stair: int, memo: dict) -> int:
        if current_stair == n:
            return 1 
        if current_stair > n:
            return 0 
        
        if current_stair in memo:
            return memo[current_stair]

        one_step = self.solve(n, current_stair + 1, memo)
        two_step = self.solve(n, current_stair + 2, memo)

        result = one_step + two_step
        memo[current_stair] = result
        return result 
        