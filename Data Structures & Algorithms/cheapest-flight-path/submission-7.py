class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))  
        maxstops = {}
        # 存储格式: (当前累计价格, 当前城市, 已经走过的边数 stops)
        pq = [(0, src, 0)]
        while pq:
            cost, node, stop = heapq.heappop(pq)
            if node == dst:
                return cost
            if stop > k:
                continue 
            if node in maxstops and maxstops[node] <= stop:
                continue 
            maxstops[node] = stop
            for nxt, w in graph[node]:
                heapq.heappush(pq, (w + cost, nxt, stop + 1)) 
        return -1 
