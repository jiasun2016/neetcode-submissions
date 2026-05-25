class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return board 
        rows, cols = len(board), len(board[0])
        q = deque([])
        for i in range(rows):
            if board[i][0] == "O":
                q.append((i, 0))
                board[i][0] = "A"
            if board[i][-1] == "O":
                q.append((i, cols-1))
                board[i][-1] = "A" 
        for j in range(cols):
            if board[0][j] == "O":
                board[0][j] = "A"
                q.append((0, j)) 
            if board[-1][j] == "O":
                board[-1][j] = "A"
                q.append((rows-1, j))
        dirs = [(0, 1), (0, -1), (1, 0),(-1, 0)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = dx + x, dy + y 
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == "O":
                    board[nx][ny] = "A"
                    q.append((nx, ny))
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"
        