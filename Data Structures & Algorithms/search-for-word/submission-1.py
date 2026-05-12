directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if not m or not n:
            return False
        if not word:
            return True

        for i in range(m):
            for j in range(n):
                # ✅ 必须从 (i, j) 作为起点
                if board[i][j] == word[0]:
                    if self.dfs(board, word, i, j, 0, set()):
                        return True
        return False

    def dfs(self, board, word, row, col, index, visited):
        # ✅ 终止条件
        if index == len(word):
            return True

        # ✅ 边界 + visited + 字符校验
        if not self.isvalid(board, row, col, index, word, visited):
            return False

        visited.add((row, col))

        for dx, dy in directions:
            if self.dfs(board, word, row + dx, col + dy, index + 1, visited):
                return True

        # ✅ 回溯
        visited.remove((row, col))
        return False

    def isvalid(self, board, i, j, index, word, visited):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if (i, j) in visited:
            return False
        return board[i][j] == word[index]
