// https://leetcode.com/problems/student-attendance-record-i

class Solution:
    def checkRecord(self, s: str) -> bool:
        if sum([1 for i in s if "A" is i or "LLL" in s])>1:
            return False
        
        return True