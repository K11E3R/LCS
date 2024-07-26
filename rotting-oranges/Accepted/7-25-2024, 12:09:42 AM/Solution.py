// https://leetcode.com/problems/rotting-oranges

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_time = 0
        
        while queue:
            x, y, time = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh_oranges -= 1
                    queue.append((nx, ny, time + 1))
                    max_time = max(max_time, time + 1)
        
        if fresh_oranges > 0:
            return -1
        
        return max_time