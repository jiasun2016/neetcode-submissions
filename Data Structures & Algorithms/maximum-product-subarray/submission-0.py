class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0] 
        curMin = 1
        curMax = 1 
         
        for num in nums:
            newMax = max(num * curMax, num * curMin, num)
            newMin = min(num * curMax , num * curMin, num) 
            curMax = newMax 
            curMin = newMin  
            res = max(res, curMax)
        return res