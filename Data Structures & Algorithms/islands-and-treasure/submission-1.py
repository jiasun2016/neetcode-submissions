class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        que = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    que.append((i,j))
        while que:
            x, y = que.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = dx+x, dy+y 
                if not self.isvalid(grid, nx, ny):
                    continue 
                grid[nx][ny] = grid[x][y]+1 
                que.append((nx, ny)) 
    def isvalid(self, grid, x, y):
        n, m = len(grid), len(grid[0]) 
        return 0 <= x < n and 0 <= y < m and grid[x][y] == 2147483647