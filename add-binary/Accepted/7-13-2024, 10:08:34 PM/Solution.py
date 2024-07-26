// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        b_s = lambda a,b : bin(int(a, 2) + int(b, 2))
        return b_s(a,b)[2:]