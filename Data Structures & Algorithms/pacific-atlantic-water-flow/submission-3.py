class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not len(heights[0]):
            return heights
        rows = len(heights)
        cols = len(heights[0])
         
        pac = [[False]*cols for _ in range(rows)]
        atl = [[False]*cols for _ in range(rows)]
        pacific = deque([])
        atlantic = deque([])
        for i in range(rows):
            pac[i][0] = True 
            pacific.append((i, 0))
            atl[i][-1] = True 
            atlantic.append((i, cols-1))
        for j in range(cols):
            pac[0][j] = True 
            pacific.append((0, j))
            atl[-1][j] = True 
            atlantic.append((rows-1, j))
        self.bfs(pacific, pac, heights)
        self.bfs(atlantic,atl, heights)
        res = []
        for i in range(rows):
            for j in range(cols):
                if pac[i][j] == True and atl[i][j] == True:
                    res.append([i,j])
        return res 
        
    def bfs(self, source, board, heights):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while source:
            x, y = source.popleft()
            for dx, dy in dirs:
                nx = dx + x 
                ny = dy + y 
                if (0 <= nx < len(board) and 0 <= ny < len(board[0]) 
                    and not board[nx][ny] 
                    and heights[nx][ny] >= heights[x][y]):
                    source.append([nx, ny])
                    board[nx][ny] = True 
            
 

                
            