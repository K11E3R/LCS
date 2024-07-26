// https://leetcode.com/problems/find-the-encrypted-string

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        updated = ''
        n = len(s)
        for i in range(n):
            updated += s[(i + k) % n]
        return updated