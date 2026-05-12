class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        res = 0
        for sell in prices:
            minP = min(sell, minP) 
            res = max(res, sell - minP) 
        return res 