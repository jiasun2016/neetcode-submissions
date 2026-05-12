directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    # dfs(board, word,now, x, y) board是字母板，word是单词，now是已经匹配了word的位置，x，y是最后一次匹配成功的字母板的位置下标
    def dfs(self, board, word, now, x, y, n, m, visited):
        dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        if now == len(word) - 1:
            return True
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] != word[now + 1] or (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            if self.dfs(board, word, now + 1, nx, ny, n, m, visited):
                return True
            visited.remove((nx, ny))
        return False
    def exist(self, board, word):
        visited = set()
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    if self.dfs(board, word, 0, i, j, n, m, visited):
                        return True
                    visited.remove((i,j))
        return False