class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0 
        visited = [False]* n
        dist = [float("inf")] * n 
        edges = 0 
        ans = 0
        while edges < n-1:
            visited[node] = True 
            x1, y1 = points[node]
            nxt = -1 
            for i in range(n):
                if visited[i]:
                    continue
                x2, y2 = points[i]
                newDist = abs(x1-x2) + abs(y1-y2)
                dist[i] = min(dist[i], newDist) 
                if nxt == -1 or dist[i] < dist[nxt]:
                    nxt = i 
            ans += dist[nxt] 
            edges += 1 
            node = nxt 
        return ans 
                 
