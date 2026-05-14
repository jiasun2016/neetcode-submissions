class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) -1
            while l < r:
                if l > i + 1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                total = nums[l] + nums[r]
                if - nums[i] == total:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1 
                    r -= 1 
                elif -nums[i] > total:
                    l += 1 
                else:
                    r -= 1 
        return res 
            