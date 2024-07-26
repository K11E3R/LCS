// https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution(object):
    def finalValueAfterOperations(self, operations):
        e = [1 if '+' in i else -1 for i in operations]
        e = sum(e)
        return e
