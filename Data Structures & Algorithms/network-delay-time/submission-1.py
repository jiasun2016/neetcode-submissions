class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v,t)) 
        dist = {i: float("inf") for i in range(1, n+1)}
        self.dfs(k, 0, dist, adj)
        res = max(dist.values())
        return res if res < float('inf') else -1

    def dfs(self, node, time, dist, adj):
        if dist[node] <= time:
            return 
        dist[node] = time
        for nei, t in adj[node]:
            self.dfs(nei, t + time, dist, adj) 
