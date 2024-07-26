// https://leetcode.com/problems/find-the-encrypted-string

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k = k % n  
        cs = [s[(i + k) % n] for i in range(n)]
        return "".join(cs)