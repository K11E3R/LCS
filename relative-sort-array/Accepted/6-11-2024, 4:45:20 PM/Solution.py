// https://leetcode.com/problems/relative-sort-array

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        order_map = {num: i for i, num in enumerate(arr2)}
        a1_a2 = []
        n_a1_a2 = []
        for num in arr1:
            if num in order_map:
                a1_a2.append(num)
            else:
                n_a1_a2.append(num)
        a1_a2.sort(key=lambda x: order_map[x]);n_a1_a2.sort()
        return a1_a2 + n_a1_a2



        