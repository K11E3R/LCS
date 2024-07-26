// https://leetcode.com/problems/height-checker

class Solution(object):
    def heightChecker(self, heights):
        return sum([1 for i, j in zip(heights, sorted(heights)) if i!=j ])
