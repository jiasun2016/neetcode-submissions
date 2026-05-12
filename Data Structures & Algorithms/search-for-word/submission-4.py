class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    if self.dfs(board, word, 1, i, j, visited):
                        return True 
                    visited.remove((i,j))
        return False 
    
    def dfs(self, board, word, now, x, y, visited):
        if now == len(word):
            return True 
        dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        n, m = len(board), len(board[0]) 
        for dx, dy in dirs:
            nx, ny = dx + x, dy + y 
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] != word[now] or (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            if self.dfs(board, word, now+1, nx, ny, visited):
                return True 
            visited.remove((nx, ny))
        return False 


        
    