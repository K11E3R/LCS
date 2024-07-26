// https://leetcode.com/problems/bitwise-and-of-numbers-range

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cur = right
        while cur > left:
            cur = cur & (cur - 1)
        return cur