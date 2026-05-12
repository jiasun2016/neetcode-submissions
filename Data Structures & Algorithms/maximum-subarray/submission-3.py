class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res, minPrefix = -float("inf"), 0
        prefix = 0  
        for num in nums:
            prefix += num
            res = max(res, prefix - minPrefix) 
            minPrefix = min(minPrefix, prefix)
        return res

