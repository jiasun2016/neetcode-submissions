class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        cnt = 0 
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: 
                    q.append((i, j)) 
                elif grid[i][j] == 1:
                    cnt += 1 
        while q and cnt:
            res += 1
            for i in range(len(q)):
                i ,j = q.popleft() 
                for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    x, y = i + a, j + b 
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1: 
                        cnt -= 1 
                        grid[x][y] = 2
                        q.append((x, y)) 
        return res if cnt == 0 else -1 

                