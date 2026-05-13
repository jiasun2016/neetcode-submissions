class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for i in range(len(nums)):
            streak = 1
            curr = nums[i]
            if curr - 1 not in seen:
                while curr + 1 in seen:
                    streak += 1 
                    curr += 1 
                res = max(streak, res)
        return res 

