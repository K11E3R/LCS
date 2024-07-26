// https://leetcode.com/problems/power-of-two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n ==1 :
            return True
        return True if not n%2 else False