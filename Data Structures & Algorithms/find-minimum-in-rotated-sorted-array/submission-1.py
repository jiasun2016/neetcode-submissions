class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1 
        while start + 1 < end:
            mid = (start+end)//2 
            if nums[end] < nums[mid]:
                start = mid 
            else:
                end = mid 
        return min(nums[start], nums[end])