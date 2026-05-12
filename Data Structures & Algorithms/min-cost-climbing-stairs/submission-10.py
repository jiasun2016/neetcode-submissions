class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n+1)
        pre1 = 0
        pre2 = 0
        for i in range(2, n+1):
            pre1, pre2 = min(pre1+cost[i-1], pre2+cost[i-2]), pre1
        return pre1