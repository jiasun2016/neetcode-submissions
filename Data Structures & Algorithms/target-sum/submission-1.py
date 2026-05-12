class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums) 
        # newtarget = (total + target)//2
        if total < target or (total + target)%2 != 0:
            return 0 
        T = (total + target)//2
        dp = [0] * (T+1) 
        dp[0] = 1 
        for num in nums:
            for j in range(T, num-1, -1):
                dp[j] += dp[j-num] 
        return dp[T]