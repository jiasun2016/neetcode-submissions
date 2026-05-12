class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        n = len(nums) 
        for i in range(n):
            prev1, prev2 = max(prev1, prev2+nums[i]), prev1
        return prev1
