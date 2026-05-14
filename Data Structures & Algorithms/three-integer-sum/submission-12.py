class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            l = i + 1
            r = len(nums)-1
            target = -nums[i]
            while l < r:
                if l > i + 1 and nums[l] == nums[l-1]:
                    l += 1
                    continue 
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif total > target:
                    r -= 1
                else:
                    l += 1
        return res 
                