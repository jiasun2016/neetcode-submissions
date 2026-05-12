class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums) 
        mySum = sum(nums);
        if mySum % 2 == 1:
            return False 
        mySum = mySum// 2
        dp = [False] * (mySum+1)
        dp[0] = True
        for i in range(n):
            for j in range(mySum, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i]] 
        return dp[mySum]
