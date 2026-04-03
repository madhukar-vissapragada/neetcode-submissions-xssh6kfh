class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.solve(amount, coins, 0, {}) 
    
    def solve(self, amount: int, coins: List[int], current_index: int, memo:dict) -> int:
        if amount == 0:
            return 1 
        if current_index == len(coins):
            return 0 
        
        current_key = (current_index, amount)
        if current_key in memo:
            return memo[current_key]

        pick = do_not_pick = 0 
        if amount - coins[current_index] >= 0:
            pick += self.solve(amount-coins[current_index], coins, current_index, memo)
        
        do_not_pick += self.solve(amount, coins, current_index + 1, memo) 
        result = pick + do_not_pick

        memo[current_key] = result 
        return result
