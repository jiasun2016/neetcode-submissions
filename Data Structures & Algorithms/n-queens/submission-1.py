class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs(n, [], res)
        return res 
    
    def dfs(self, n, cols, res):
        row = len(cols)
        if len(cols) == n:
            res.append(self.genBoard(cols)) 
            return 
        for col in range(n):
            if not self.isvalid(cols,row,col):
                continue 
            cols.append(col) 
            self.dfs(n, cols, res)
            cols.pop()

    def genBoard(self, cols):
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
        return board 
    def isvalid(self, cols, row, col):
        for i in range(len(cols)):
            j = cols[i]
            if  col == j:
                return False 
            if i + j == row + col or i - j == row - col:
                return False 
        return True
