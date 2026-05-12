class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        visited.add((0, 0))
        dirs = [[0,1],[1,0], [-1,0],[0,-1]] 
        minH = [(grid[0][0], 0, 0)]
        while minH: 
            time, x, y = heapq.heappop(minH)
            if x == n-1 and y == n-1:
                return time 
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy 
                if (0 <= nx < n and 0 <= ny < n and 
                    (nx, ny) not in visited):
                    visited.add((nx, ny))
                    maxTime = max(grid[nx][ny], time)
                    heapq.heappush(minH, (maxTime, nx, ny))
            