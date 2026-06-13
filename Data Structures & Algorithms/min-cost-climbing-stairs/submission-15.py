class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)
        pre1 = 0
        pre2 = 0

        for i in range(2,n+1):
            curr = min(pre1+ cost[i-2], pre2+cost[i-1]) 
            pre1 = pre2 
            pre2 = curr
        return curr