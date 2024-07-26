// https://leetcode.com/problems/optimal-partition-of-string

class Solution:
    def partitionString(self, s: str) -> int:
        seen_chars = set()
        count = 1
        
        for c in s:
            if c in seen_chars:
                count += 1
                seen_chars.clear()
            seen_chars.add(c)
        
        return count
