class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        dists = [float("inf")]* (n+1)
        for u, v, w in times:
            edges[u].append([v, w])
        dists[k] = 0 
        q = [(0, k)]
        while q:
            dist, curr = heapq.heappop(q)
            if dist > dists[curr]:
                continue 
            for nxt, w in edges[curr]:
                newDist = w + dist
                if newDist <  dists[nxt]:
                    dists[nxt] = newDist
                    heapq.heappush(q, [newDist, nxt])
        ans = max(dists[1:])
        return ans if ans != float("inf") else -1 