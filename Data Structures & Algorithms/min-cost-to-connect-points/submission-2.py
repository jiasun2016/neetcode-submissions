class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # 当前所在的点
        if n <= 1:
            return 0
        # 当前所在的点（Prim 从任意一点开始，这里从 0 开始）
        node = 0
        # dist[i]：当前“生成树”到第 i 个点的最小连接成本
        dist = [float("inf")] * n
        # 第 i 个点是否已经加入最小生成树 
        visit = [False] * n
        # edges：已经加入的边数
        # res：最小生成树的总成本
        edges, res = 0, 0 
        while edges < n - 1: 
            # 将当前点加入生成树
            visit[node] = True 
             # 当前点的坐标
            x1, y1 = points[node] 
            # 寻找下一个要加入生成树的点，init to -1 方便更新
            nextNode = -1
            # 尝试用当前点到所有“未加入生成树”的连接成本打擂台
            # 并找出最小连接成本
            for i in range(n):
                if visit[i]:
                    continue
                x2, y2 = points[i]
                # 当前点到第 i 个点的曼哈顿距离
                curDist = abs(x1 - x2) + abs(y1 - y2)
                # 如果通过当前点连接 i 更便宜，就更新 dist[i]
                dist[i] = min(dist[i], curDist)
                # 在所有未访问的点中，选 dist 最小的那个作为下一个点
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i 
            # 将最小代价的边加入结果
            res += dist[nextNode]
            # 更新当前点为新加入的点
            node = nextNode
            # 已使用边数 +1
            edges += 1
        # 返回最小生成树的总成本
        return res



