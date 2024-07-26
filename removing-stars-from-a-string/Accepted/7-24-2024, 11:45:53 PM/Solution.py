// https://leetcode.com/problems/removing-stars-from-a-string

class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        for x in s:
            if x is "*":
                result.pop()
            else:
                result.append(x)
        return "".join(result)

        