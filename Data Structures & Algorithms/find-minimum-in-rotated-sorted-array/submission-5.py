class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l + 1 < r:
            mid = l + (r-l)//2 
            if nums[mid] > nums[r]:
                l = mid 
            else:
                r = mid 
        return min(nums[l],nums[r])