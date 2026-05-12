class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0 , 1
        lens = len(prices)
        maxP = 0
        while r < lens: 
            maxP = max(maxP, prices[r]-prices[l])
            if prices[l] > prices[r]:
                l = r 
            r += 1 
        return maxP

            
