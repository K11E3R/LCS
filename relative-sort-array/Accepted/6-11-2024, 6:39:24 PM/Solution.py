// https://leetcode.com/problems/relative-sort-array

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        om1 = [nn for nn in arr1 if nn not in {nn: i for i, nn in enumerate(arr2)}]
        om2 = [nn for nn in arr1 if nn in {nn: i for i, nn in enumerate(arr2)}]
        ommm = sorted(om2, key=lambda x: {nn: i for i, nn in enumerate(arr2)}[x]) + sorted(om1) 
        return ommm   