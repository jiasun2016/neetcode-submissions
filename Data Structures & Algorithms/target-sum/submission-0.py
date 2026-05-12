class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Edge cases
        if total_sum < target or (target + total_sum) % 2 != 0:
            return 0
        
        S = (target + total_sum) // 2
        
        # Initialize DP array
        dp = [0] * (S + 1)
        dp[0] = 1  # There's one way to make sum 0: select no elements
        
        for num in nums:
            # Traverse backwards to ensure each num is only used once
            for j in range(S, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[S]