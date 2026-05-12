class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp[i] 表示：从第 i 阶开始，走到楼顶的最小花费
        # 楼顶不算台阶，所以 dp[n] 和 dp[n+1] 都是 0
        dp = [0] * (n + 2)
        # 从后往前计算，因为 dp[i] 由 dp[i+1] 和 dp[i+2] 决定
        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        # 可以从第 0 阶或第 1 阶开始，选更小的
        return min(dp[0], dp[1])
