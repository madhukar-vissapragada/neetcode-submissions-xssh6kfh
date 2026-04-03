class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = self.solve(coins, amount, 0, {})
        return -1 if result >= 100000 else result

    def solve(self, coins: List[int], amount: int, current_index: int, memo: dict) -> int:
        if amount == 0:
            return 0
        if current_index == len(coins):
            return 100000

        current_key = (current_index, amount)
        if current_key in memo:
            return memo[current_key]

        pick = 100000
        if amount - coins[current_index] >= 0:
            pick = 1 + self.solve(coins, amount - coins[current_index], current_index, memo)
        do_not_pick = self.solve(coins, amount, current_index + 1, memo)

        result = min(pick, do_not_pick)
        memo[current_key] = result 
        return result
