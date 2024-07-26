// https://leetcode.com/problems/the-kth-factor-of-n

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        a = [i for i in range(1, n+1) if not n%i]
        return a[k-1] if len(a)>= k else -1