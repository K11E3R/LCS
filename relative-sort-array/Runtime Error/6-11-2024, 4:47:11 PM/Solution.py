// https://leetcode.com/problems/relative-sort-array

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        return sorted([num for num in arr1 if num in {num: i for i, num in enumerate(arr2)}], key=lambda x: order_map[x]) + sorted(num for num in arr1 if num not in {num: i for i, num in enumerate(arr2)})