// https://leetcode.com/problems/crawler-log-folder

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if log == "../":
                if count > 0:
                    count -= 1
            elif log != "./":
                count += 1
        return count
