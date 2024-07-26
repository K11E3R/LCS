// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution:
    def findMinArrowShots(self, p: List[List[int]]) -> int:
        return (q:=-inf) and sum((q<s,q:=e if q<s else min(q,e))[0] for s,e in sorted(p))

with open("user.out", "w") as f:
    for points in map(loads, stdin):
        s = Solution()
        f.write(f"{s.findMinArrowShots(points)}\n")
exit(0)