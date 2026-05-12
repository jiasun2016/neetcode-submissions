class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1 
        while start+ 1 < end:
            mid = start + (end - start)//2 
            if nums[end] < nums[mid]:
                start = mid
            else:
                end = mid
        return min(nums[start],nums[end])

                
