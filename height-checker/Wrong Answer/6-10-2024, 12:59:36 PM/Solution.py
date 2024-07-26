// https://leetcode.com/problems/height-checker

class Solution(object):
    def heightChecker(self, heights):
        c = 0
        if max(heights) == heights[0] and heights[0] != heights[1]:
            return len(heights)
        for i in range(len(heights)-1):
            if heights[i]>heights[i+1]:
                heights[i], heights[i+1] = heights[i+1], heights[i]
                c+=1
        return c