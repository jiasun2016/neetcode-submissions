class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
     
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    if self.dfs(board, word, i, j,0, visited):
                        return True 
                    visited.remove((i,j)) 
        return False 
    def dfs(self, board, word, i, j, index, visited):
        if index == len(word)-1:
            return True 
        dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        for dx, dy in dirs:
            nx, ny = dx + i, dy + j
            if (nx, ny) in visited:
                continue 
            if not self.isValid(board, nx, ny):
                continue 
            if board[nx][ny] != word[index+1]:
                continue
            visited.add((nx, ny))
            if self.dfs(board, word, nx, ny, index+1, visited):
                return True
            visited.remove((nx, ny))
    def isValid(self, board, x, y):
        n,m = len(board), len(board[0])
        return 0 <= x < n and 0 <= y < m


            