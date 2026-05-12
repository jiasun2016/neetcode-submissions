class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        mySum = sum(nums)
        if mySum%2==1:
            return False 
        target = mySum//2 
        dp = [[False] * (target+1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            for j in range(target +1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j] 
        return dp[n][target]
