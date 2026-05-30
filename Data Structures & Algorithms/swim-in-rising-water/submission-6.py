import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        # (time, x, y)
        heap = [(grid[0][0], 0, 0)]
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]
        while heap:
            t, x, y = heapq.heappop(heap)
            if x == n - 1 and y == n - 1:
                return t
            # 关键：跳过过期状态（标准 Dijkstra）
            if t > dist[x][y]:
                continue
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    nt = max(t, grid[nx][ny])
                    if nt < dist[nx][ny]:
                        dist[nx][ny] = nt
                        heapq.heappush(heap, (nt, nx, ny))