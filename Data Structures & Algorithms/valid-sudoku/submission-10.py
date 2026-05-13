class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] in seen:
                    return False 
                if board[row][i] == ".":
                    continue 
                seen.add(board[row][i])
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] in seen:
                    return False 
                if board[i][col] == ".":
                    continue 
                seen.add(board[i][col]) 
        for sequre in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (sequre//3)*3 + i
                    col = (sequre%3)*3 + j 
                    if board[row][col] in seen:
                        return False 
                    if board[row][col] == ".":
                        continue 
                    seen.add(board[row][col])
        return True 

