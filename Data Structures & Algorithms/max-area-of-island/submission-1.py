class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    are = self.bfs(grid, i, j)
                    maxArea = max(maxArea, are) 

        return maxArea 
    def bfs(self, grid, x, y):
        size = 1 
        grid[x][y] = 0 
        que = deque([(x, y)])  
        while que:
            x, y = que.popleft()
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]: 
                nx, ny = dx + x, dy+y 
                if not self.isValid(grid, nx, ny):
                    continue
                size+=1 
                grid[nx][ny] = 0   
                que.append((nx, ny)) 
        return size 
    def isValid(self, board, x, y):
        n, m = len(board), len(board[0]) 
        return 0 <= x and x< n and 0 <= y and y < m and board[x][y] == 1
        




