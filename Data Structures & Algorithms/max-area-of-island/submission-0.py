class Solution:
    
    
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0 
        maxSize = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxSize = max(self.bfs(grid, i, j), maxSize)
                    
        return maxSize 

    def bfs(self, grid, x, y):
        queue = collections.deque([(x, y)]) 
        grid[x][y] = 0
        maxSize = 1
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                nx = dx + x 
                ny = dy + y 
                if not self.isValid(grid, nx, ny):
                    continue 
                queue.append((nx, ny))
                maxSize += 1
                print("maxSize")
                grid[nx][ny] = 0
        return maxSize

    def isValid(self, board, x, y):
        n, m = len(board), len(board[0]) 
        return 0 <= x and x< n and 0 <= y and y < m and board[x][y] == 1
