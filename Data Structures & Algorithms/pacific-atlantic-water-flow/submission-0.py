class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0]) 
        
        pac = [[False] * m for _ in range(n)] 
        atl = [[False] * m for _ in range(n)] 
        pacific = []  
        atlantic = [] 
        for r in range(n):
            pacific.append((r, 0))
            pac[r][0] = True 
            atlantic.append((r,  m-1))
            atl[r][m-1] = True 

        for c in range(m):
            pacific.append((0, c))
            pac[0][c] = True 
            atlantic.append((n - 1, c))
            atl[n-1][c] = True 
            
        self.bfs(pacific, pac, heights) 
        self.bfs(atlantic, atl, heights) 
        res = []
        for i in range(n):
            for j in range(m):
                if pac[i][j] == atl[i][j] == True:
                    res.append([i, j]) 
        return res

    def bfs(self, source, ocean, heights):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        q = deque(source) 
        while q: 
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < len(ocean) and 0 <= nc < len(ocean[0]) and 
                    not ocean[nr][nc] and 
                    heights[nr][nc] >= heights[r][c]
                ):
                    q.append((nr, nc)) 
                    ocean[nr][nc] = True 
        
