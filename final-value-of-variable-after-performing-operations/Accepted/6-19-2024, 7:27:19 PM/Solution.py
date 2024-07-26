// https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution(object):
    def finalValueAfterOperations(self, operations):
        
        s = 0
        for i in operations:
            if i in ["X++", "++X"]:
                s+=1
            else:
                s-=1

        return s
        # a = {"+": 1, "-":-1}
        # e = [1 if '+' in i else -1 for i in operations]
        # return sum(e)
