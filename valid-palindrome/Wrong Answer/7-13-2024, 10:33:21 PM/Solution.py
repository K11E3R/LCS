// https://leetcode.com/problems/valid-palindrome

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        x =(re.sub(r'[^\w]','',s)).lower()
        print(x)
        if x == x[::-1] :
            return True
        return False