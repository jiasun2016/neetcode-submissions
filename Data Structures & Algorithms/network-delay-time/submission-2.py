class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph[u] = [(v, w), ...] 
        graph = defaultdict(list)
        for src, dst, travel_time in times:
            graph[src].append((dst, travel_time))
        # min_time[node] = min time from k(start) to node 
        min_time = [float("inf")] * (n + 1)
        min_time[k] = 0
        # (current_time, node)
        min_heap = [(0, k)] 
        while min_heap:
            current_time, node = heapq.heappop(min_heap)
            # 如果已经找到更短路径，跳过当前状态
            if current_time > min_time[node]:
                continue
            for neighbor, edge_time in graph[node]:
                new_time = current_time + edge_time
                # 找到更短路径就更新
                if new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))

        answer = max(min_time[1:])
        return answer if answer < float("inf") else -1
