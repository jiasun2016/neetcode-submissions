class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        for n in nums:
            streak = 1 
            cur = n
            while cur + 1 in store:
                streak += 1 
                cur += 1 
            res = max(streak, res)
        return res 
            
