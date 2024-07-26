// https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3: return n
        mod = 10**9 + 7
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1], dp[2] = 1, 1, 2
        triminoes = 0
        for j in range(3, n+1):
            triminoes += 2*dp[j-3]
            triminoes %= mod
            dp[j] = dp[j-1] + dp[j-2] + triminoes
        return dp[-1] % mod