class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = [1] + nums + [1] 
        n = len(nums)
        dp = [[0]*n for _ in range(n)] 
        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i + l -1 
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j]) 
        return dp[0][n-1]

