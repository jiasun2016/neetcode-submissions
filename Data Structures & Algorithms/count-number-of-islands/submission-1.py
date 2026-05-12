class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        if not grid or not grid[0]:
            return count 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j) 
                    count += 1 
        return count  
    def bfs(self, board, i, j):  
        board[i][j] = "0"
        que = deque([(i, j)])
        while que:
            x, y = que.popleft() 
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                nx, ny = dx + x, dy + y 
                if not self.isvalid(board, nx, ny):
                    continue 
                board[nx][ny] = "0"
                que.append((nx, ny))

    def isvalid(self, board, x, y):
        n, m = len(board), len(board[0]) 
        return 0 <= x and x< n and 0 <= y and y < m and board[x][y] == "1"
            


