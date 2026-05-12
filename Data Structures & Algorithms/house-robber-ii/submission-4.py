class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        if len(nums) <= 2:
            return max(nums) 
        dp = [0] * 3
        n = len(nums)
        # dp[0], dp[1] = 0, nums[1]

        for i in range(1, n):
            dp[i%3] = max(dp[(i-2)%3]+ nums[i], dp[(i-1)%3])
        ans = dp[(n-1)%3]
        dp = [0] * 3
        # dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(0, n-1):
            dp[i%3] = max(dp[(i-2)%3]+ nums[i], dp[(i-1)%3])

        return max(dp[(n-2)%3], ans) 
