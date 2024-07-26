// https://leetcode.com/problems/student-attendance-record-i

class Solution:
    def checkRecord(self, s: str) -> bool:
        if 'LLL' in s:
            return "The student was late 3 consecutive days in the last 3 days, so is not eligible for the award."
        
        
        if sum([1 for i in s if "A" is i])>1:
            return "The student was late 3 consecutive days in the last 3 days, so is not eligible for the award."
        
        return "The student has fewer than 2 absences and was never late 3 or more consecutive days."