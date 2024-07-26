// https://leetcode.com/problems/relative-sort-array

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        om = {nn: i for i, nn in enumerate(arr2)}
        om1 = [nn for nn in arr1 if nn not in om]
        om2 = sorted([nn for nn in arr1 if nn in om], key=lambda x : om[x])
        
        return om2+ sorted(om1)
   