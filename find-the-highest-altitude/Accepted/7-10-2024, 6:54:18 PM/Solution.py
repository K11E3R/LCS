// https://leetcode.com/problems/find-the-highest-altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = [0]
        [a.append(a[-1] + i) for i in gain]
        return max(a)