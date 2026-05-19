class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        if not word:
            return True
        if not rows:
            return False 
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = "#"
                    if self.dfs(board, i, j, 1, word):
                        return True 
                    board[i][j] = temp 
        return False 
    def dfs(self, board, x, y, index, word):
        if index == len(word):
            return True 
        dirs = [[0,1], [0,-1], [1, 0],[-1, 0]]
        for dx, dy in dirs:
            nx = dx + x 
            ny = dy + y 
            if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                continue 
             
            if board[nx][ny] == word[index]:
                temp = word[index] 
                board[nx][ny] = "#"
                if self.dfs(board, nx, ny, index+1, word):
                    return True 
                board[nx][ny] = temp
        return False 


