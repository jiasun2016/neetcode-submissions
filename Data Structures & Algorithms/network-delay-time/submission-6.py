class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dists = [float("inf")] * (n+1)
        adjs = collections.defaultdict(list)
        for u, v, w in times:
            adjs[u].append((v,w))
        q = [(0, k)]
        dists[k] = 0 
        while q:
            dist, curr = heapq.heappop(q)
            if dist > dists[curr]:
                continue 
            for nxt, w in adjs[curr]:
                newDist = w + dist 
                if newDist < dists[nxt]:
                    dists[nxt] = newDist
                    heapq.heappush(q,(newDist, nxt)) 
        ans = max(dists[1:])
        return ans if ans != float("inf") else -1