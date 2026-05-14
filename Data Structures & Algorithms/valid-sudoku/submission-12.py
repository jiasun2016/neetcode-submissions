class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols,rows, sqrs = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set) 
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in cols[j]:
                    return False 
                cols[j].add(val)
                if val in rows[i]:
                    return False
                rows[i].add(val)
                if val in sqrs[(i//3, j//3)]:
                    return False 
                sqrs[(i//3, j//3)].add(val) 
        return True 