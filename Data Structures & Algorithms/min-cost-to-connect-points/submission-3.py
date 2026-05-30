class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        dist = [100000000] * n
        visit = [False] * n
        edges, res = 0, 0

        while edges < n - 1:
            visit[node] = True
            nextNode = -1
            x1, y1 = points[node]
            for i in range(n):
                if visit[i]:
                    continue
                x2, y2 = points[i]
                curDist = (abs(x1 - x2) + abs(y1 - y2))
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
                    
            res += dist[nextNode]
            node = nextNode
            edges += 1

        return res