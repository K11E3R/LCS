// https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution(object):
    def finalValueAfterOperations(self, operations):
        return sum([1 if '+' in i else -1 for i in operations])
