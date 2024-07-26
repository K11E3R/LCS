// https://leetcode.com/problems/find-the-encrypted-string

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        cs = list(s)
        for i in range(len(s)):
            cs[i] = s[(i + k) % len(s)]
        return "".join(cs)