// https://leetcode.com/problems/height-checker

class Solution(object):
    def heightChecker(self, heights):
        a = [i for i in heights];a.sort()
        return sum([ 1 for i in range(len(heights)) if a[i] != heights[i]])
