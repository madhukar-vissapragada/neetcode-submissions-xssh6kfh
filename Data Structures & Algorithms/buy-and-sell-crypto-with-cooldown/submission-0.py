class Solution:
    def maxProfit(self,prices: List[int]) -> int:
        return self.solve(prices, 0, 1, {})
    
    def solve(self, prices: List[int], current_index: int, can_buy: int, memo: dict) -> int:
        if current_index >= len(prices):
            return 0 
        
        current_key = (current_index, can_buy)
        if current_key in memo:
            return memo[current_key]
        
        idle = self.solve(prices, current_index + 1, can_buy, memo)
        buy = sell = 0
        if can_buy:
            buy = -(prices[current_index]) + self.solve(prices, current_index + 1, 0, memo)
        else:
            sell = (prices[current_index]) + self.solve(prices, current_index + 2, 1, memo)
        
        result = max(idle, (buy + sell))
        memo[current_key] = result
        return result
