// https://leetcode.com/problems/diagonal-traverse

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up = True
        rows = len(mat)
        cols = len(mat[0]) 
        res = []

        i ,j = 0, 0

        while i < rows and j < cols:
            res.append(mat[i][j])

            if up:
                if j == cols - 1:
                    up = False
                    i += 1
                elif i == 0:
                    up = False
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == rows - 1:
                    up = True
                    j += 1
                elif j == 0:
                    up = True
                    i += 1
                else:
                    i += 1
                    j -= 1
        
        return res