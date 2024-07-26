// https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m_len = len(word1) if len(word1) < len(word2) else len(word2)
        a = "".join([word1[i] + word2[i] for i in range(m_len)])
        aa = "".join(word2[m_len:] if len(word1) < len(word2) else word1[m_len:])
        return a + aa
