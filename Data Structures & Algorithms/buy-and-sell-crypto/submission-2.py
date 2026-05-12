class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 
        minBuy = float("inf") 
        for price in prices:
            minBuy = min(price, minBuy) 
            maxP = max(maxP, price - minBuy) 
        return maxP
