class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProift = 0 
        minP = prices[0]
        for p in prices:
            minP = min(p, minP) 
            maxProift = max(p - minP, maxProift)  
        return maxProift
        