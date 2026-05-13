class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, sqrs = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set) 
        for r in range(9):
            for c in range(9):
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in sqrs[(r//3,c//3)]):
                    return False
                if board[r][c] == ".":
                    continue 
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                sqrs[(r // 3, c // 3)].add(board[r][c])
        return True 