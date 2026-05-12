class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            target = - nums[i] 
            l,r = i+1, len(nums)-1 
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1 
                else:
                    ans.append([-target, nums[l], nums[r]]) 
                    while l < r and nums[l] == nums[l+1]:
                        l+= 1 
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1 
                    l += 1
                    r -= 1 
        return ans 