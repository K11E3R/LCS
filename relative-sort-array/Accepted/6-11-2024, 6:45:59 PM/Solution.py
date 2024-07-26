// https://leetcode.com/problems/relative-sort-array

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        om = {num: i for i, num in enumerate(arr2)}
        return sorted(filter(lambda x: x in om, arr1), key=lambda x: om[x]) + sorted(filter(lambda x: x not in om, arr1))
