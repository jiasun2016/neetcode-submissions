class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n+1)
        adjs = collections.defaultdict(list)
        for u, v, w in times:
            adjs[u].append((v,w)) 
        dist[k] = 0 
        q = [(0, k)]
        while q:
            d, curr = heapq.heappop(q) 
            if d >  dist[curr]:
                continue 
            for nxt, w in adjs[curr]:
                newDist = w + d
                if newDist < dist[nxt]:
                    dist[nxt] = newDist  
                    heapq.heappush(q, (newDist, nxt))
        res = max(dist[1:])
        return res if res != float("inf") else -1 

                