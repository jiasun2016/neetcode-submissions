class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for L in range(3, n+1):
            for l in range(n - L + 1):
                r = l + L -1
                for k in range(l+1, r):
                    dp[l][r] = max(dp[l][r],
                    dp[l][k] + dp[k][r] + nums[l] * nums[k] * nums[r]
                    )
        return dp[0][n-1]