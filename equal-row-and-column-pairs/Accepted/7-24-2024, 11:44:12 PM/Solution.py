// https://leetcode.com/problems/equal-row-and-column-pairs

class Solution:                                
    def equalPairs(self, grid: List[List[int]]) -> int:
        tp = Counter(zip(*grid))                
        h = Counter(map(tuple,grid))           
        return  sum(tp[t]*h[t] for t in tp) 