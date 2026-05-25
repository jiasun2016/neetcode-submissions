class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        count = 0
        if not grid or not grid[0]:
            return 0
        que = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    que.append((i,j))
                elif grid[i][j] == 1:
                    count += 1
        while que and count:
            time += 1 
            level = len(que)
            for i in range(level):
                x, y = que.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = dx+x, dy+y 
                    if self.isvalid(nx, ny, grid): 
                        grid[nx][ny] = 2
                        count -= 1 
                        que.append((nx,ny))
            
        return time if count == 0 else -1;
    def isvalid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y] == 1