// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = 0
        robby = 0
        for i in nums:
            temp = rob
            rob = max(robby + i, rob)
            robby = temp
        return max(rob, robby)