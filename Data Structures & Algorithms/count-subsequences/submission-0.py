class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s) 
        m = len(t) 
        if m > n:
            return 0 
        dp = [[0]* (m+1) for i in range(n+1)]  
        for i in range(n+1):
            dp[i][0] = 1 

        for i in range(n):
            for j in range(m):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i][j] 
                else:
                    dp[i+1][j+1] = dp[i][j+1] 
        return dp[n][m]