class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = len(nums) - k
        return self.partition(0, len(nums)-1, nums, index)

    def partition(self, start, end, nums, k):
        left, right = start, end 
        pivot = nums[(start+end)//2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
        if k <= right:
            return self.partition(start, right, nums, k)
        elif k >= left:
            return self.partition(left, end, nums, k) 
        return nums[k]

