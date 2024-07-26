// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int(''.join(map(str, digits))) + 1
        return list(map(int, str(a)))