class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        lens = len(nums)
        for i in range(lens-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            self.findTwoSum(nums, i+1, lens-1, -nums[i], res)
        return res 
    def findTwoSum(self, nums, l, r, target, res):
        while l < r:
            temp = nums[l] + nums[r]
            if temp < target:
                l += 1 
            elif temp > target:
                r -= 1 
            else:
                res.append([-target, nums[l], nums[r]])
                l += 1 
                r -= 1 
                while l < r and nums[l] == nums[l-1]:
                    l += 1 
                while l < r and nums[r] == nums[r+1]:
                    r -= 1 
                
            
