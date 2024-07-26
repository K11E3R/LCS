// https://leetcode.com/problems/subarray-sums-divisible-by-k

from collections import defaultdict

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        r, p, d = 0, 0, {0: 1}
        for num in nums:
            p = (p + num) % k
            r += d.get(p, 0)
            d[p] = d.get(p, 0) + 1
        return r
        """
        r, p, d = 0, 0, defaultdict(int, {0: 1})
        for num in nums:
            p = (p + num) % k
            r += d[p]
            d[p] += 1
        return r
