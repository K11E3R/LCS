// https://leetcode.com/problems/relative-sort-array

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        count = [0] * 1001
        result = []
        
        for num in arr1:
            count[num] += 1
        
        for num in arr2:
            result.extend([num] * count[num])
            count[num] = 0
        
        for i in range(1001):
            result.extend([i] * count[i])
        
        return result
