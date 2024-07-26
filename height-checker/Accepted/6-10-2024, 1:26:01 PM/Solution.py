// https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c = 0
        a = [i for i in heights]; a.sort()
        for i in range(len(heights)):
            if a[i] != heights[i]:
                c+=1
        return c
