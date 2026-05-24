class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0 
        islands = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j) 
                    islands+= 1 
        return islands  
    def bfs(self, grid, x, y):
        q = collections.deque([(x,y)])
        grid[x][y] = "0"
        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                nx, ny = dx + x, dy + y
                if not self.isValid(grid, nx, ny):
                    continue
                q.append((nx, ny))
                grid[nx][ny] = "0"
    def isValid(self, board, x, y):
        n, m = len(board), len(board[0]) 
        return 0 <= x and x< n and 0 <= y and y < m and board[x][y] == "1"
