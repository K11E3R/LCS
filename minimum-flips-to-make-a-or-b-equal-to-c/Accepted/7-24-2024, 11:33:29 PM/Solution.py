// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return ((a | b) ^ c).bit_count() + (a & b & ((a | b) ^ c)).bit_count()