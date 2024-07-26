// https://leetcode.com/problems/largest-number-at-least-twice-of-others

from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        max1 = float('-inf')
        max2 = float('-inf')
        index1 = -1
        
        for i, num in enumerate(nums):
            if num > max1:
                max2 = max1
                max1 = num
                index1 = i
            elif num > max2:
                max2 = num
        
        if max1 >= 2 * max2:
            return index1
        else:
            return -1