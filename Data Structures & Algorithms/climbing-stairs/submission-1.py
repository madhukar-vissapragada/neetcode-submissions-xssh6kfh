class Solution:
    def climbStairs(self, n: int) -> int:
        return self.solve(0, n, {}) 
    
    def solve(self, current_stair:int, n:int, map:dict) -> int:
        if current_stair == n:
            return 1
        
        if current_stair > n:
            return 0

        current_key = current_stair
        if current_key in map:
            return map[current_key]
    
        one_step = self.solve(current_stair + 1, n, map)
        two_step = self.solve(current_stair + 2, n, map)

        result = one_step + two_step
        map[current_key] = result

        return result
    