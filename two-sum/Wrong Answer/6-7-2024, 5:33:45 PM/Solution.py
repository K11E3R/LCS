// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            s = 0
            l = []
            for j in range(i, len(nums)):
                s += nums[j]
                l.append(j)
                if s == target:
                    return l
