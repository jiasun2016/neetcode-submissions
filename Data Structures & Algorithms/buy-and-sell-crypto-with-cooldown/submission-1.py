class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0 
        n = len(prices)
        buy = [0]* n
        sell = list(buy) 
        cooldown = list(sell)
        buy[0] = - prices[0]
        for i in range(1, n):
            cooldown[i] = sell[i-1]
            sell[i] = max(sell[i-1] , buy[i-1] + prices[i]) 
            buy[i] = max(buy[i-1], cooldown[i - 1] - prices[i])
        return max(sell[-1], cooldown[-1])
