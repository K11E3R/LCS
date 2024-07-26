// https://leetcode.com/problems/height-checker

class Solution(object):
    def heightChecker(self, heights):
        c = 0
        a = [i for i in heights]; a.sort()
        a = [1 for i in range(len(heights)) if a[i] != heights[i]]
        # for i in range(len(heights)):
        #     if a[i] != heights[i]:
        #         c+=1
        return sum(a)
