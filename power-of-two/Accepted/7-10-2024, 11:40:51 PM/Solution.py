// https://leetcode.com/problems/power-of-two

class Solution:
    def isPowerOfTwo(self, x: int) -> bool:
        return True if x>0 and (x & (x - 1)) == 0 else False