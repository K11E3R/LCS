// https://leetcode.com/problems/valid-palindrome

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        x =(re.sub(r'[^a-zA-Z0-9]','',s)).lower()
        if x == x[::-1] :
            return True
        return False