class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1 
        while l + 1 < r:
            mid = l + (r-l)//2 
            if nums[mid] > nums[r]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid 
                else:
                    l = mid 
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid 
                else:
                    r = mid 
        if nums[l] == target:
            return l 
        if nums[r] == target:
            return r 
        return -1