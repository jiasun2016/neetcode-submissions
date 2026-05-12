class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # if n == 1:
        #     return cost[0]
        # # dp[i] = 到达第 i 阶的最小花费
        # dp = [0] * n
        # dp[0] = cost[0]
        # dp[1] = cost[1]
        # for i in range(2, n):
        #     dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        # # 从倒数第一或第二阶迈上楼顶
        # return min(dp[n - 1], dp[n - 2]) 
        prev2 = cost[0]  # dp[0]
        prev1 = cost[1]  # dp[1]
        for i in range(2, n):
            curr = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr

        return min(prev1, prev2)
