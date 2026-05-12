class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1 
        ans = [1] * len(nums) 
        for i in range(len(nums)):
            ans[i] = prefix * ans[i] 
            prefix = prefix*nums[i]  
        prefix = 1 
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i] * prefix 
            prefix = prefix * nums[i]

        return ans
