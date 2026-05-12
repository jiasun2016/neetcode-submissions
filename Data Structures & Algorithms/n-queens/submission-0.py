class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs(n, [], res) 
        return res 

    def dfs(self, n, cols, result):
        row = len(cols)
        if len(cols) == n:
            result.append(self.draw_chessboard(cols)) 
            return 
        for col in range(n):
            if not self.is_valid(cols, row, col):
                continue 
            cols.append(col) 
            self.dfs(n, cols, result) 
            cols.pop() 
            
    def draw_chessboard(self, cols):
        n = len(cols) 
        board = []
        for i in range(n):
            row = []
            for j in range(n):
                if cols[i] == j:
                    row.append("Q") 
                else:
                    row.append(".") 
            
            board.append("".join(row)) 
            print(board)
        return board  
    def is_valid(self, cols, row, col):
        for i in range(len(cols)):
            j = cols[i] 
            if j == col:
                return False 
            if i + j == row + col or i - j == row - col:
                return False 
        return True
