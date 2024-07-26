// https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort()
        verticalCut.sort()
        
        # test max gap
        max_horizontal_gap = self.calculate_max_gap(m, horizontalCut)
        max_vertical_gap = self.calculate_max_gap(n, verticalCut)
        
        # test mod 48
        MOD = 10**9 + 7
        total_cost = (max_horizontal_gap * max_vertical_gap) % MOD
        
        return total_cost
    
    def calculate_max_gap(self, length: int, cuts: List[int]) -> int:
        max_gap = cuts[0]  
        for i in range(1, len(cuts)):
            max_gap = max(max_gap, cuts[i] - cuts[i-1])
        
        max_gap = max(max_gap, length - cuts[-1])
        
        return max_gap