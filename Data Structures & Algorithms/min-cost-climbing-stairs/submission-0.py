class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.solve(0, cost, {}), self.solve(1, cost, {}))

    def solve(self, current_stair: int, cost: List[int], map: dict) -> int:
        if current_stair == len(cost):
            return 0
            
        current_key = current_stair 

        if current_key in map:
            return map[current_key]

        if current_stair < len(cost):
            one_step = cost[current_stair] + self.solve(current_stair + 1, cost, map)
            two_step = cost[current_stair] + self.solve(current_stair + 2, cost, map)

            result = min(one_step, two_step)

            map[current_key] = result
            return result

        return 100000