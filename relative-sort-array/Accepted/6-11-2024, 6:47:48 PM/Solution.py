// https://leetcode.com/problems/relative-sort-array

from collections import defaultdict

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        relative_order = defaultdict(list)
        
        for i, num in enumerate(arr2):
            relative_order[num] = [i, num]
        
        # Sort arr1 based on the relative order in arr2, and the remaining elements in ascending order
        return sorted(arr1, key=lambda x: relative_order.get(x, [float('inf'), x]))
