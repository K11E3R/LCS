// https://leetcode.com/problems/find-the-town-judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge=[0]*1001
        nums={i for i in range(1,n+1)}
        for tr in trust:
            judge[tr[1]]+=1
            nums.discard(tr[0])
        for i in nums:
            if judge[i]==n-1: return i
        return -1
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(Solution().findJudge(nums, next(inputs)),file=f)
exit(0)