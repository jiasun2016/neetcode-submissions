class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs(n, res, [])
        return res 
    
    def dfs(self, n, res, cols):
        if len(cols) == n:
            res.append(self.genboard(cols)) 
            return 
        row = len(cols)
        for col in range(n):
            if self.isvalid(row, col, n, cols):
                cols.append(col)
                self.dfs(n, res, cols)
                cols.pop() 
    def isvalid(self, row, col, n, cols):
        for i in range(len(cols)):
            j = cols[i]
            if i + j == row + col or i - j == row - col or col == j:
                return False 
        return True 
    def genboard(self, cols):
        res = []
        for i in range(len(cols)):
            row = ""
            for j in range(len(cols)):
                if cols[i] == j:
                    row += "Q"
                else:
                    row += "." 
            res.append(row)
        return res

    