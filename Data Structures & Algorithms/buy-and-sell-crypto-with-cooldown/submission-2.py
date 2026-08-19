class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0 
        n = len(prices)
        # 1. 初始化三个状态数组，分别记录每天对应状态的最大收益
        buy = [0] * n
        sell = list(buy)      # [0] * n
        cooldown = list(sell) # [0] * n
        # 2. Base Case（第 0 天的基础状态）
        buy[0] = -prices[0]   # 第 0 天买入股票，收益为 -prices[0]
        # sell[0] 和 cooldown[0] 默认为 0（第 0 天不持股/冷冻期收益为 0）
        # 3. 状态转移递推
        for i in range(1, n):
            # cooldown[i] 依赖前一天的 sell 状态
            cooldown[i] = sell[i-1]
            # sell[i] 可以选择继续不持股，或者今天把前一天的股票卖掉
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]) 
            # buy[i] 可以选择继续持股，或者在前一天冷冻期结束后今天买入
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i])
            
        # 4. 最终的最大收益一定出现在不持股的状态（卖出或冷冻期）
        return max(sell[-1], cooldown[-1])