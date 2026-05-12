DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWs, COLS = len(board), len(board[0]) 
        visited = set() 
        for r in range(ROWs):
            for c in range(COLS):
                if self.dfs(r, c, 0, board, word, visited):
                    return True 
        return False

    def dfs(self, r, c, i, board, word, visited):
        if i == len(word):
            return True 
        ROWs, COLS = len(board), len(board[0]) 
        if (r < 0 or r >= ROWs or
            c < 0 or c >= COLS or
            (r, c) in visited or
            board[r][c] != word[i]):
            return False
        visited.add((r,c)) 
        rws = False
        for dx, dy in DIRS:
            x = dx + r 
            y = dy + c
            if self.dfs(x, y, i+ 1, board, word, visited): 
                return True
        visited.remove((r,c))  
        return False

