// https://leetcode.com/problems/three-consecutive-odds

import numpy as np

class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        arr = np.array(arr)
        odds = arr % 2 == 1
        return np.any(odds[:-2] & odds[1:-1] & odds[2:])
