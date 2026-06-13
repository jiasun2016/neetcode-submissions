class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        times = [[float("inf")]* n for i in range(n)]
        times[0][0] = grid[0][0]
        q = [(grid[0][0], 0, 0)]
        while q:
            time, x, y = heapq.heappop(q)
            if x == n-1 and y == n-1:
                return time
            if time > times[x][y]:
                continue 
            for dx, dy in [(0, 1), (1, 0),(0, -1), (-1, 0)]:
                nx,ny = dx + x, dy + y 
                if 0 <= nx < n and 0 <= ny < n:
                    newTime = max(grid[nx][ny], time)
                    if newTime < times[nx][ny]:
                        times[nx][ny] = newTime 
                        heapq.heappush(q, (newTime, nx, ny))


