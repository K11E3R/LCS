// https://leetcode.com/problems/koko-eating-bananas

import math as m
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            hours_required = sum(m.ceil(pile / mid) for pile in piles)
            if hours_required > h:
                low = mid + 1
            else:
                high = mid
        return low