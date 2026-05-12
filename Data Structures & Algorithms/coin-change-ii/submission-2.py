class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]* (amount+1) for i in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(0, amount + 1):
                dp[i][j] += dp[i-1][j]
                a = coins[i-1] 
                if j >= a:
                    dp[i][j] += dp[i][j-a]
        return dp[n][amount]
                

