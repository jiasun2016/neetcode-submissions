class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if not num -1 in numSet:
                lens = 1
                while num + lens in numSet:
                    lens += 1
                longest = max(longest, lens) 
        return longest