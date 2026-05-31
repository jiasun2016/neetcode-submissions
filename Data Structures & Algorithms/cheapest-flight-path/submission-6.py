class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        pq = [(0, src, 0)]
        max_stops = {}
        while pq:
            price, node, stops = heapq.heappop(pq)
            if node == dst:
                return price
            if stops > k:
                continue
                
            if node in max_stops and max_stops[node] <= stops:
                continue
            max_stops[node] = stops
            
            for neighbor, weight in graph[node]:
                heapq.heappush(pq, (price + weight, neighbor, stops + 1))
                
        return -1