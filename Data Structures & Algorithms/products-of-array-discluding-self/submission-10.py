class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]* n
        pref = 1

        for i in range(n):
            res[i] = pref 
            pref *= nums[i] 
        suff = 1
        for i in range(n-1, -1, -1):
            res[i] *= suff
            suff *= nums[i] 
        return res

