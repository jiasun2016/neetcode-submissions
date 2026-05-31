class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * (n)
        dist[src] = 0
        for i in range(k+1):
            preDist = list(dist)
            for u, v, w in flights:
                if preDist[u] != float('inf') and preDist[u] + w < dist[v]:
                    dist[v] = preDist[u] + w 
        return dist[dst] if dist[dst] != float('inf') else -1 

