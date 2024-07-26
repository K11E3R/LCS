// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = 1
        if n < 0:
            print(f"n val : {n} != {x}")
            x = 1/x
            print(f"n val : {n} != {x}")

        for i in range(n):
            p = p * x
        return p