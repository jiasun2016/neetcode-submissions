class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        minP = prices[0]
        for p in prices:
            minP = min(minP, p) 
            ans = max(ans, p - minP) 
        return ans 