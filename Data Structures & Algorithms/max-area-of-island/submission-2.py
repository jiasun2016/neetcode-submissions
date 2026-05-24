class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0 
        maxAre = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    size = self.bfs(grid, i, j) 
                    maxAre= max(maxAre, size)
        return maxAre  
    def bfs(self, grid, i, j):
        grid[i][j] = 0
        size = 1
        q = collections.deque([(i, j)])
        while q:
            x, y = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = dx + x, dy + y 
                if not self.isValid(grid, nx, ny):
                    continue 
                size += 1
                grid[nx][ny] = 0
                q.append((nx, ny))
        return size 
    def isValid(self, board, x, y):
        n, m = len(board), len(board[0]) 
        return 0 <= x and x< n and 0 <= y and y < m and board[x][y] == 1
