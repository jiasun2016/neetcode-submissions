class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in dic:
                lens = 1
                while num + lens in dic:
                    lens += 1
                longest = max(longest, lens) 
        return longest

                