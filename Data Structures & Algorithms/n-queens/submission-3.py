class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        self.dfs(n, [], ans)
        return ans 

    def dfs(self, n, cols, ans):
        if len(cols) == n:
            ans.append(self.genRes(cols))
            return 
        
        for i in range(n):

            valid = True

            for r, c in enumerate(cols):

                # 同列
                if c == i:
                    valid = False
                    break

                # 对角线
                if abs(r - len(cols)) == abs(c - i):
                    valid = False
                    break

            if not valid:
                continue

            cols.append(i)

            self.dfs(n, cols, ans)

            cols.pop()

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