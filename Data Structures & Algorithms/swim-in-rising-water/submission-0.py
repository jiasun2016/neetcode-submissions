class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid) 
        visited = set()
        visited.add((0, 0))
        directions = [[0,1],[1,0], [-1,0],[0,-1]]
        minH = [(grid[0][0], 0, 0)] 
        while minH:
            t, r, c = heapq.heappop(minH) 
            if r == n-1 and c == n-1:
                return t
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if (nr < 0 or nr >= n or nc < 0 or 
                    nc >= n or (nr, nc) in visited):
                    continue 
                visited.add((nr,nc)) 
                heapq.heappush(minH, (max(grid[nr][nc], t), nr, nc)) 
            