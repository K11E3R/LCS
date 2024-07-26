// https://leetcode.com/problems/subarray-sums-divisible-by-k

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        b = []
        a = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i:len(nums)-j] :
                    a.append(nums[i:len(nums)-j])
        for i in a :
            if not sum(i)%k:
                b.append(i)
        return len(b)