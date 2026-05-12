class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 0 
        i = 0 
        lens = 0 
        curr = nums[0]
        
        while i < len(nums):
            if curr!= nums[i]:
                curr = nums[i]
                lens = 0 
            while i < len(nums) and curr == nums[i]:
                i += 1 
            curr += 1 
            lens += 1  
            longest = max(longest, lens)
        return longest 