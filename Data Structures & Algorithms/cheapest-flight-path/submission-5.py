class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 1. 经典开局：构建邻接表
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
            
        # 2. 优先队列 (Min-Heap)
        # 存储状态格式: (当前累计价格, 当前城市, 剩余可走边数)
        # 最多中转 K 次 ＝ 最多能走 K + 1 条边
        pq = [(0, src, k + 1)]
        
        # 3. 核心剪枝账本：记录到达该城市时，历史上最大的“剩余可走边数”
        # 格式：{ 城市 node: 历史上最大剩余边数 }
        max_remaining_stops = {}
        while pq:
            price, node, stops_left = heapq.heappop(pq)
            
            # 目标终点退出机制（Early Stopping）：
            # 由于是优先队列，第一个被弹出来的 dst 绝对是满足步数约束下的全局最低价
            if node == dst:
                return price
                
            # 如果当前路径已经把边数用尽了，无法再向下扩展邻居
            if stops_left <= 0:
                continue
                
            # 👑 动态剪枝核心：
            # 如果你不是第一次来这个城市，且你现在剩的步数还不如历史最多的时候多，直接乱棍淘汰
            if node in max_remaining_stops and max_remaining_stops[node] >= stops_left:
                continue
            # 更新该城市能达到的最大续航记录
            max_remaining_stops[node] = stops_left
            
            # 4. 扩展邻居
            for neighbor, weight in graph[node]:
                # 塞入优先队列，价格累加，剩余边数减 1
                heapq.heappush(pq, (price + weight, neighbor, stops_left - 1))
                
        return -1