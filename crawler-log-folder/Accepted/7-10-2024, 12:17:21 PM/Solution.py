// https://leetcode.com/problems/crawler-log-folder

import re
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in logs :
            if count<0:
                count =0
            if "./" == i:
                continue
            if "../" in i:
                count -= 1
            else:
                count +=1                
            print(f"count : {count} elem : {i}")
        return count if count>0 else 0