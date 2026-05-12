class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0 
        prod = 1
        ans = [0]* len(nums)
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zeros += 1 

        if zeros > 1:
            return ans 
        for i in range(len(nums)):
            if nums[i] == 0:
                ans[i] = prod 
            elif zeros == 0:
                ans[i] = prod//nums[i] 
        return ans 

                
         
