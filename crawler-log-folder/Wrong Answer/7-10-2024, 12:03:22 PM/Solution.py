// https://leetcode.com/problems/crawler-log-folder

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = -1
        for i in logs :
            if "." in i :
                continue
            else :
                count+=1
        return count