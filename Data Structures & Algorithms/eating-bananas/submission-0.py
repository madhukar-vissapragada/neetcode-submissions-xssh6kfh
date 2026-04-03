import math
from typing import *


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        min_rate = sum(piles)
        while low <= high:
            mid = (low + high) // 2
            result = self.is_minimum(piles, h, mid)
            if result:
                high = mid - 1
                min_rate = mid
            else:
                low = mid + 1

        return min_rate

    def is_minimum(self, piles: List[int], h: int, current_rate: int) -> bool:
        current_pile_time = lambda total_bananas: math.ceil(total_bananas / current_rate)

        total_time = 0
        for current_pile in piles:
            total_time += current_pile_time(current_pile)

        if total_time <= h:
            return True

        return False
