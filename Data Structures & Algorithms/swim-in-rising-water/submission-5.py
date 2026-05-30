class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        q = [(grid[0][0], 0, 0)]
        visited.add((0, 0))
        dirs = [[0, 1], [1, 0],[0, -1], [-1, 0]]
        while q:
            h, x, y = heapq.heappop(q)
            if x == n-1 and y == n-1:
                return h  
            for dx, dy in dirs:
                nx, ny = dx + x, dy + y 
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    maxH = max(grid[nx][ny], h) 
                    visited.add((nx, ny))
                    heapq.heappush(q, (maxH, nx, ny))
            