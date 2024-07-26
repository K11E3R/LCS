// https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights):
        a = heights.copy();a.sort()
        return sum([ 1 for i in range(len(heights)) if a[i] != heights[i]])

