// https://leetcode.com/problems/optimal-partition-of-string

from collections import Counter as cc

class Solution:
    def partitionString(self, s: str) -> int:
        return max([i for _,i in cc(s).items()])
