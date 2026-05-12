class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        pre2 = 0 # dp[n]，站在楼顶，不需要花钱
        pre1 = 0 # dp[n-1]，从最后一阶之后到楼顶，花费为 0
        # 从后往前算 dp[i] 
        for i in range(n-1, -1, -1):
            curr = min(pre1, pre2) + cost[i] 
            pre2 = pre1 
            pre1 = curr 
        # 可以从第 0 或第 1 阶开始
        return min (pre1, pre2)
