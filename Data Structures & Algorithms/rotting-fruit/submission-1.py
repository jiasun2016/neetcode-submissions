class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        que = deque([])
        cnt = 0 
        time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: 
                    que.append((i, j)) 
                elif grid[i][j] == 1: 
                    cnt += 1 
        while que and cnt:
            time += 1
            for i in range(len(que)):
                x, y = que.popleft()
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        nx, ny = dx +x , dy + y 
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                            que.append((nx, ny))
                            cnt -= 1 
                            grid[nx][ny] = 2 

        return time if cnt == 0 else -1

                


        