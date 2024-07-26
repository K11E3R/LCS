// https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort()
        verticalCut.sort()
        
        def max_gap(length, cuts):
            max_gap_val = cuts[0]
            for i in range(1, len(cuts)):
                max_gap_val = max(max_gap_val, cuts[i] - cuts[i-1])
            return max(max_gap_val, length - cuts[-1])
        
        MOD = 10**9 + 7
        max_h_gap = max_gap(m, horizontalCut)
        max_v_gap = max_gap(n, verticalCut)
        
        return (max_h_gap * max_v_gap) % MOD