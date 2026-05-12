
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0 
        buy = [0 for _ in range(len(prices))]
        sell = list(buy)
        cooldown = list(buy) 
        buy[0] = -prices[0] 
        for i in range(1, len(prices)):
            cooldown[i] = sell[i - 1]
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(buy[i - 1], cooldown[i - 1] - prices[i])
            
        return max(sell[-1], cooldown[-1])