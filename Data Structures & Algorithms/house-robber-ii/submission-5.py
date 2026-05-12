class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        if len(nums) <= 2:
            return max(nums) 
        return max(self.helper(nums[1:]),
                   self.helper(nums[:-1]))
    def helper(self, nums):
        dp = [0] * 3
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        n = len(nums)
        for i in range(1, n):
            dp[i%3] = max(dp[(i-2)%3]+ nums[i], dp[(i-1)%3])

        return dp[(n-1)%3]
