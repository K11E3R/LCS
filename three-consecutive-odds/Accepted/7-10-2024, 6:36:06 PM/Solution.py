// https://leetcode.com/problems/three-consecutive-odds

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
            count = count + 1 if num % 2 else 0
            if count == 3:
                return True
        return False
