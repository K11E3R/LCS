// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ind = 0
        for i in range(n + 1):
            while ind < n and nums[ind] < i:
                ind += 1
            if n - ind == i:
                return i
            # if n - ind < i:
            #     return -1
        return -1
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(Solution().specialArray(nums),file=f)
exit(0)