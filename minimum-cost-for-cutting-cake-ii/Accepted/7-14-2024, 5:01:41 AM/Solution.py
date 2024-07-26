// https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        
        h_index, v_index = 0, 0
        h_pieces, v_pieces = 1, 1
        total_cost = 0
        
        while h_index < len(horizontalCut) and v_index < len(verticalCut):
            if horizontalCut[h_index] >= verticalCut[v_index]:
                total_cost += horizontalCut[h_index] * v_pieces
                h_index += 1
                h_pieces += 1
            else:
                total_cost += verticalCut[v_index] * h_pieces
                v_index += 1
                v_pieces += 1
        
        while h_index < len(horizontalCut):
            total_cost += horizontalCut[h_index] * v_pieces
            h_index += 1
        
        while v_index < len(verticalCut):
            total_cost += verticalCut[v_index] * h_pieces
            v_index += 1
        
        return total_cost