class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        dp = [False]* n 
        dp[0] = True 
        for i in range(n):
            for j in range(i):
                if j + nums[j] >= i and dp[j]:
                    dp[i] = True 
        return dp[n-1]