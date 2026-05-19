class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        self.dfs(n, [], ans)
        return ans 
    def dfs(self, n, cols, ans):
        if len(cols) == n:
            ans.append(self.genRes(cols))
            return 
        row = len(cols)
        for col in range(n):
            if self.isvalid(row, col, n, cols):
                cols.append(col)
                self.dfs(n, cols, ans)
                cols.pop()
    def isvalid(self, row, col, n, cols):
        for i in range(len(cols)):
            j = cols[i]
            # if i + j == row + col or i - j == row - col or col == j:
            if abs(i - row) == abs(col - j) or col == j:
                return False 
        return True
    def genRes(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            sub = ""
            for j in range(n):
                if cols[i] == j:
                    sub += "Q"
                else:
                    sub += "." 
            board.append(sub)
        return board 



                    
                    
