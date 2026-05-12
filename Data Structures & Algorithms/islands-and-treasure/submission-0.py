
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return grid 
        n, m = len(grid), len(grid[0])
        queue = collections.deque() 
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i,j)) 
        
        while queue:
            x, y = queue.popleft()  
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = dx+x, dy+y 
                if not self.isValid(nx, ny, grid, visited):
                    continue 
                queue.append((nx, ny))
                visited.add((nx, ny))
                grid[nx][ny] = grid[x][y] +1 
        

    def isValid(self, x, y, grid, visited):
        n, m = len(grid), len(grid[0]) 
        return 0 <= x < n and 0 <= y < m and grid[x][y] == 2147483647 and (x, y) not in visited
