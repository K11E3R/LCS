// https://leetcode.com/problems/height-checker

class Solution(object):
    def heightChecker(self, heights):
        a = [1 for i, j in zip(heights, sorted(heights)) if i!=j ]
        return sum(a)
