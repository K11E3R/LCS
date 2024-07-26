// https://leetcode.com/problems/decremental-string-concatenation

from typing import List

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        dp = [[float('inf')] * 26 for _ in range(26)]
        dp[ord(words[0][0]) - ord('a')][ord(words[0][-1]) - ord('a')] = len(words[0])
        
        for i in range(1, n):
            s = words[i]
            a, b = ord(s[0]) - ord('a'), ord(s[-1]) - ord('a')
            new_dp = [[float('inf')] * 26 for _ in range(26)]
            
            for x in range(26):
                for y in range(26):
                    if dp[x][y] < float('inf'):
                        new_dp[x][b] = min(new_dp[x][b], dp[x][y] + len(s) - (y == a))
                        new_dp[a][y] = min(new_dp[a][y], dp[x][y] + len(s) - (x == b))
            
            dp = new_dp
        
        return min(min(row) for row in dp)