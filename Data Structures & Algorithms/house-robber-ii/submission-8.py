class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def helper(nums):
            n = len(nums)
            prev1, prev2 = 0, 0 
            for i in range(n):
                prev1, prev2 = max(prev1, prev2+nums[i]), prev1
            return prev1
        
        return max(helper(nums[1:]), helper(nums[:-1]))
        

        
    