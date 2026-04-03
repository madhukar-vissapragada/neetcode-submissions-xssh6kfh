class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.solve(0, nums, {})
    
    def solve(self, current_house, houses: List[int], map:dict) -> int:
        if current_house >= len(houses):
            return 0 
        
        rob = 0
        do_not_rob = 0

        current_key = current_house
        if current_key in map:
            return map[current_key]

        rob = (houses[current_house] + self.solve(current_house + 2, houses, map))
        do_not_rob += self.solve(current_house + 1, houses, map)

        result = max(rob, do_not_rob)
        map[current_key] = result
        
        return result
