class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        mySum =  sum(nums);
        if mySum % 2 == 1:
            return False
        mySum = mySum//2
        dp = [False for x in range(mySum+1)]
        dp[0] = True
        for i in range(0,length):
            newDp = list(dp)
            for j in range(mySum+1):
                newDp[j] = dp[j] or dp[j - nums[i]]
            dp = newDp
            
        return dp[mySum]