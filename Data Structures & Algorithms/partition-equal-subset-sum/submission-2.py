class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        lens = len(nums)
        mySum = sum(nums)
        if mySum%2==1:
            return False 
        mySum = mySum//2 
        dp = [False] * (mySum+1) 
        dp[0] = True
        for i in range(lens):
            old = list(dp) 
            for j in range(mySum +1):
                if j >= nums[i]:
                    dp[j] = old[j] or old[j-nums[i]]
                else:
                    dp[j] = old[j] 
        return dp[mySum]
