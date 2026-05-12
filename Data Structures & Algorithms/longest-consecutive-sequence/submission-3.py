class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums) 
        streak = 0 
        res = 0
        for num in nums:
            if num - 1 not in store:
                streak = 0
                curr = num 
                while curr in store:
                    streak += 1 
                    curr += 1 
            res = max(res, streak)
        return res
            
