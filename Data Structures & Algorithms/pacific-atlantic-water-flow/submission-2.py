class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0]) 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        pac = [[False]* cols for _ in range(rows)]
        atl = [[False]* cols for _ in range(rows)] 
        pacific = deque([]) 
        atlantic = deque([])
        for c in range(cols):
            pacific.append((0,c))
            pac[0][c] = True 
            atlantic.append((rows-1, c))
            atl[rows-1][c] = True  
        for r in range(rows):
            pacific.append((r, 0))
            pac[r][0] = True 
            atlantic.append((r, cols-1))
            atl[r][cols-1] = True 
        self.bfs(pacific, pac, heights)
        self.bfs(atlantic, atl, heights) 
        res = []
        for i in range(rows):
            for j in range(cols):
                if pac[i][j] == atl[i][j] == True:
                    res.append([i, j]) 
        return res
    def bfs(self, source, board, heights):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        while source: 
            x, y = source.popleft()
            for dx, dy in directions:
                nx, ny = dx + x, dy + y 
                if (0 <= nx < len(board) and 0 <= ny < len(board[0]) and
                    not board[nx][ny] and heights[nx][ny] >= heights[x][y]):
                    board[nx][ny] = True 
                    source.append((nx, ny)) 





