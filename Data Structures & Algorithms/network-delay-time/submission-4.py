class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append([v, w])
        minDist = [float("inf")]* (n+1)
        minDist[k] = 0 
        q = [(0, k)]
        while q:
            dist, curr = heapq.heappop(q)
            if dist > minDist[curr]:
                continue
            for nxt, w in edges[curr]:
                newDist = w + dist 
                if newDist < minDist[nxt]:
                    minDist[nxt] = newDist 
                    heapq.heappush(q, (newDist, nxt))
        ans = max(minDist[1:])
        return -1 if ans == float("inf") else ans