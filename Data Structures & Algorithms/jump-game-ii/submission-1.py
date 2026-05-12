class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        #dp[i]表示跳到下标为i的位置最少需要几次跳跃
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                # 如果从j可以到跳到i
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] +1) 
                    break
        return dp[n-1]