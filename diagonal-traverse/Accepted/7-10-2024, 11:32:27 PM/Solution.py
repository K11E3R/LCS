// https://leetcode.com/problems/diagonal-traverse

from typing import List, Dict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        
        diagonals: Dict[int, List[int]] = {}
        rows, cols = len(mat), len(mat[0])
        
        # Populate the hashmap with diagonals
        for r in range(rows):
            for c in range(cols):
                if (r + c) not in diagonals:
                    diagonals[r + c] = []
                diagonals[r + c].append(mat[r][c])
        
        result = []
        
        for key in sorted(diagonals.keys()):
            if key % 2 == 0:
                result.extend(reversed(diagonals[key]))
            else:
                result.extend(diagonals[key])
        
        return result