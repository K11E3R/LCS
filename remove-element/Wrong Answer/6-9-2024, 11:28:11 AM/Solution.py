// https://leetcode.com/problems/remove-element

class Solution(object):
    def removeElement(self, n, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        o=n.count(val)
        n.remove(val)
        print(o,', nums = ',n)
    
        