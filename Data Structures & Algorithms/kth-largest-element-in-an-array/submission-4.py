class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = len(nums) - k 
        return self.partition(0, len(nums)-1, nums, index)
    
    def partition(self, start, end, nums, k):
        l, r = start, end 
        pivot = nums[l + (r-l)//2]
        print(pivot, nums)
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1 
            while l <= r and nums[r] > pivot:
                r -= 1  
            if l <= r :
                nums[l], nums[r] = nums[r], nums[l]
                l += 1 
                r -= 1 
        if k <= r:
            return self.partition(start, r, nums, k)
        elif k >= l:
            return self.partition(l, end, nums, k)
        print(l, r, nums)
        return nums[k]
