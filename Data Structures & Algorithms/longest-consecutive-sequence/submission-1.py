class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set(nums)
        res = 0 
        for num in nums:
            curr = num 
            streak = 0 
            while curr in nums:
                curr += 1 
                streak += 1 
            res = max(res, streak) 
        return res
        