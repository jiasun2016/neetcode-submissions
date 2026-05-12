class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        if len(nums) <= 2:
            return max(nums) 
        
        n1 = self. helper(nums, 0, len(nums)-1, [0]*3) 
        n2 = self. helper(nums, 1, len(nums), [0]*3) 
        return max(n1, n2)
        

    def helper(self, nums, start, end, dp):
        for i in range(start, end):
            dp[i%3] = max(dp[(i-1)%3], dp[(i-2)%3] + nums[i]) 
        return max(dp[(end-1)%3], dp[(end-2)%3])
        
