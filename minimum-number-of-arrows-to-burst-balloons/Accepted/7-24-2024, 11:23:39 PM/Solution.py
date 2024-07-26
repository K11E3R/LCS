// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution:
    def findMinArrowShots(self, p: List[List[int]]) -> int:
        return (q:=-inf) and sum((q<s,q:=e if q<s else min(q,e))[0] for s,e in sorted(p))