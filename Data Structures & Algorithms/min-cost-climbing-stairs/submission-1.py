class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.solve(cost, 0, {}), 
                self.solve(cost, 1, {})) 
    
    def solve(self, cost: List[int], current_stair, memo) -> int:
        if current_stair >= len(cost):
            return 0 
        
        if current_stair in memo:
            return memo[current_stair]
        
        one_step = cost[current_stair] + self.solve(cost, current_stair + 1, memo) 
        two_step = cost[current_stair] + self.solve(cost, current_stair + 2, memo)

        result = min(one_step, two_step)
        memo[current_stair] = result
        return result
